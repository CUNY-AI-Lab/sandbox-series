"""
title: Adventure Kit
description: Render participant-defined choice adventures with declared state, conditions, effects and endings. No built-in adventure.
version: 2.1.0
"""

import json
import math
import re

from fastapi.responses import HTMLResponse

THEMES = ("cuny-blue", "linux-terminal", "classic-arcade", "bauhaus")
SPEEDS = {"instant": 0, "slow": 35, "medium": 75, "fast": 140}
MAX_BYTES = 500_000
MAX_ERRORS = 12
ID_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9_-]{0,79}")
RESERVED_IDS = {"constructor", "prototype", "__proto__"}
ID_RULE = "start with a letter, then use letters, digits, _ or -, 80 characters at most"
KINDS = {
    "boolean": "true or false",
    "number": "a number",
    "text": "text",
    "list": "a list of text",
}
NO_ADVENTURE = (
    "No adventure was supplied. Ask the participant for their adventure topic or setting, "
    "available choices, and goals or open-ended preference. Use their material to propose "
    "rules for confirmation. Do not launch or substitute a default adventure."
)
CONVERT = (
    "Use adventure schema_version 2. Convert existing scenario content with participant "
    "approval; do not silently replace it."
)


# ---------- small checks shared by the validator ----------


def _kind(value):
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, str):
        return "text"
    if isinstance(value, list):
        return "list"
    return "unsupported"


def _valid_value(value):
    kind = _kind(value)
    if kind == "number":
        return math.isfinite(value)
    if kind == "text":
        return len(value) <= 6000
    if kind == "list":
        return len(value) <= 200 and all(
            isinstance(x, str) and len(x) <= 1000 for x in value
        )
    return kind == "boolean"


def _text(value, limit=12000):
    return isinstance(value, str) and value.strip() != "" and len(value) <= limit


def _valid_id(value):
    return (
        isinstance(value, str)
        and value not in RESERVED_IDS
        and ID_PATTERN.fullmatch(value) is not None
    )


def _describe(value):
    return KINDS.get(_kind(value), "an unsupported value")


# ---------- reading the model's input ----------


def _reject_constant(name):
    raise ValueError(f"{name} is not allowed")


def _load(text):
    return json.loads(text, parse_constant=_reject_constant)


def _parse(raw):
    """Accept an object, JSON text, fenced JSON, JSON inside other text, or JSON encoded twice."""
    if raw is None:
        return None, {
            "status": "needs_context",
            "message": NO_ADVENTURE,
            "schema_version": 2,
        }
    if isinstance(raw, dict):
        try:
            raw = json.dumps(raw, allow_nan=False)
        except ValueError:
            return None, {
                "status": "invalid_input",
                "message": "Use finite numbers only. Resend corrected JSON without replacing its content.",
            }
    if not isinstance(raw, str):
        return None, {
            "status": "invalid_input",
            "message": "Send the adventure as JSON in scenario_json.",
        }
    text = raw.strip()
    if not text:
        return None, {
            "status": "needs_context",
            "message": NO_ADVENTURE,
            "schema_version": 2,
        }
    if len(text.encode("utf-8")) > MAX_BYTES:
        return None, {
            "status": "invalid_input",
            "message": "Adventure JSON must be at most 500 KB.",
        }
    fence = re.fullmatch(r"```[A-Za-z]*\s*(.*?)\s*```", text, re.S)
    if fence:
        text = fence.group(1)
    data = None
    for attempt in (text, text[text.find("{") : text.rfind("}") + 1]):
        try:
            data = _load(attempt)
            if isinstance(data, str):
                data = _load(data)
            break
        except (ValueError, RecursionError):
            data = None
    if isinstance(data, dict) and "nodes" not in data:
        for key in ("scenario", "scenario_json", "adventure"):
            if isinstance(data.get(key), dict):
                data = data[key]
                break
    if not isinstance(data, dict):
        return None, {
            "status": "invalid_input",
            "message": "Adventure JSON could not be parsed. Resend corrected JSON without replacing its content.",
        }
    return data, None


def _normalize(s):
    """Fill harmless gaps so a small omission never blocks play. Returns a problem or None."""
    version = s.get("schema_version")
    if (
        version == 2
        or version == "2"
        or (version is None and "nodes" in s and "rooms" not in s)
    ):
        s["schema_version"] = 2
    else:
        return {"status": "invalid_input", "message": CONVERT}
    for key in ("objective", "global_choices", "sources"):
        if s.get(key) is None:
            s.pop(key, None)
    if s.get("state") is None:
        s["state"] = {}
    nodes = s.get("nodes")
    if (
        isinstance(nodes, list)
        and nodes
        and all(isinstance(n, dict) and isinstance(n.get("id"), str) for n in nodes)
    ):
        if len({n["id"] for n in nodes}) == len(nodes):
            s["nodes"] = {n["id"]: n for n in nodes}
    missing = [
        k
        for k in ("title", "introduction", "start", "nodes", "endings")
        if s.get(k) is None
    ]
    if missing:
        return {
            "status": "needs_context",
            "message": "Adventure is incomplete. Request or confirm missing fields.",
            "missing_fields": missing,
        }
    choice_lists = (
        list(s.get("nodes").values()) if isinstance(s.get("nodes"), dict) else []
    )
    for node in choice_lists:
        if isinstance(node, dict) and node.get("choices") is None:
            node["choices"] = []
    every_choice = [
        c
        for n in choice_lists
        if isinstance(n, dict) and isinstance(n["choices"], list)
        for c in n["choices"]
    ]
    if isinstance(s.get("global_choices"), list):
        every_choice += s["global_choices"]
    for choice in every_choice:
        if isinstance(choice, dict):
            for key in ("to", "when", "effects", "blocked_text", "hidden"):
                if key in choice and choice[key] is None:
                    del choice[key]
    return None


# ---------- validation with exact paths ----------


class _Checker:
    def __init__(self, scenario):
        self.s = scenario
        self.errors = []
        self.state = None
        self.nodes = {}
        self.choice_ids = set()
        self.choice_count = 0

    def flag(self, path, problem):
        if len(self.errors) < MAX_ERRORS:
            self.errors.append(f"{path}: {problem}")

    def run(self):
        s = self.s
        if not _text(s["title"], 160):
            self.flag("title", "write a title of 1 to 160 characters")
        if not _text(s["introduction"]):
            self.flag("introduction", "write an introduction of 1 to 12,000 characters")
        state = s["state"]
        if isinstance(state, dict) and len(state) <= 200:
            self.state = state
            for key, value in state.items():
                if not _valid_id(key):
                    self.flag(f"state.{key}", ID_RULE)
                if not _valid_value(value):
                    self.flag(
                        f"state.{key}",
                        "use true or false, a number, text, or a list of text",
                    )
        else:
            self.flag(
                "state",
                "declare state as an object of at most 200 keys, or {} for none",
            )
        nodes = s["nodes"]
        if isinstance(nodes, dict) and 1 <= len(nodes) <= 200:
            self.nodes = nodes
        else:
            self.flag(
                "nodes", "declare nodes as an object of 1 to 200 nodes keyed by node id"
            )
        if not isinstance(s["start"], str) or s["start"] not in self.nodes:
            self.flag("start", "name the id of the first node")
        for node_id, node in self.nodes.items():
            path = f"nodes.{node_id}"
            if not _valid_id(node_id):
                self.flag(path, ID_RULE)
            if not isinstance(node, dict):
                self.flag(
                    path, "write each node as an object with name, text and choices"
                )
                continue
            if not _text(node.get("name"), 160):
                self.flag(f"{path}.name", "write a name of 1 to 160 characters")
            if not _text(node.get("text")):
                self.flag(f"{path}.text", "write the scene text")
            self.choices(node["choices"], f"{path}.choices")
        if "global_choices" in s:
            self.choices(s["global_choices"], "global_choices")
        if self.choice_count > 1000:
            self.flag("nodes", "use at most 1,000 choices in all")
        self.endings(s["endings"])
        if "objective" in s and not _text(s["objective"], 2000):
            self.flag(
                "objective",
                "write an objective of 1 to 2,000 characters or leave it out",
            )
        if "sources" in s:
            self.sources(s["sources"])
        return self.errors

    def choices(self, items, path):
        if not isinstance(items, list) or len(items) > 80:
            self.flag(path, "use a list of at most 80 choices, or [] for none")
            return
        self.choice_count += len(items)
        for index, choice in enumerate(items):
            here = f"{path}[{index}]"
            if not isinstance(choice, dict):
                self.flag(
                    here, "write each choice as an object with id, label and text"
                )
                continue
            choice_id = choice.get("id")
            if not _valid_id(choice_id):
                self.flag(f"{here}.id", ID_RULE)
            elif choice_id in self.choice_ids:
                self.flag(
                    f"{here}.id",
                    f"'{choice_id}' repeats, and choice ids must be unique across the adventure",
                )
            else:
                self.choice_ids.add(choice_id)
            if not _text(choice.get("label"), 240):
                self.flag(f"{here}.label", "write a label of 1 to 240 characters")
            if not _text(choice.get("text")):
                self.flag(
                    f"{here}.text", "write the result text shown after this choice"
                )
            if "to" in choice and (
                not isinstance(choice["to"], str) or choice["to"] not in self.nodes
            ):
                self.flag(f"{here}.to", "name an existing node id")
            if "when" in choice:
                self.condition(choice["when"], f"{here}.when")
            if "blocked_text" in choice and not _text(choice["blocked_text"]):
                self.flag(
                    f"{here}.blocked_text",
                    "write the text shown when the condition fails",
                )
            if "hidden" in choice and not isinstance(choice["hidden"], bool):
                self.flag(f"{here}.hidden", "use true or false")
            if "effects" in choice:
                self.effects(choice["effects"], f"{here}.effects")

    def condition(self, cond, path, depth=0):
        if depth >= 20:
            self.flag(path, "nest conditions at most 20 levels deep")
            return
        if not isinstance(cond, dict) or len(cond) != 1:
            self.flag(
                path, 'write one operator per condition, such as {"eq": ["key", value]}'
            )
            return
        op, arg = next(iter(cond.items()))
        if op in ("all", "any"):
            if not isinstance(arg, list) or not 1 <= len(arg) <= 50:
                self.flag(f"{path}.{op}", "list 1 to 50 conditions")
                return
            for index, item in enumerate(arg):
                self.condition(item, f"{path}.{op}[{index}]", depth + 1)
            return
        if op == "not":
            self.condition(arg, f"{path}.not", depth + 1)
            return
        if op not in ("eq", "ne", "gt", "gte", "lt", "lte", "includes"):
            self.flag(
                path,
                f"'{op}' is not an operator, so use all, any, not, eq, ne, gt, gte, lt, lte or includes",
            )
            return
        here = f"{path}.{op}"
        if not isinstance(arg, list) or len(arg) != 2 or not isinstance(arg[0], str):
            self.flag(here, 'write ["state_key", value]')
            return
        if self.state is None:
            return
        key, want = arg
        if key not in self.state:
            self.flag(here, f"'{key}' is not declared in state")
            return
        have = self.state[key]
        if not _valid_value(want):
            self.flag(
                here, "compare with true or false, a number, text, or a list of text"
            )
        elif op in ("gt", "gte", "lt", "lte") and (
            _kind(have) != "number" or _kind(want) != "number"
        ):
            self.flag(
                here, f"{op} compares numbers, and '{key}' holds {_describe(have)}"
            )
        elif op == "includes" and (_kind(have) != "list" or not isinstance(want, str)):
            self.flag(
                here,
                f"includes needs a list key and a text value, and '{key}' holds {_describe(have)}",
            )
        elif op in ("eq", "ne") and _kind(want) != _kind(have):
            self.flag(
                here,
                f"'{key}' holds {_describe(have)}, so compare it with {_describe(have)}",
            )

    def effects(self, items, path):
        if not isinstance(items, list) or len(items) > 50:
            self.flag(path, "use a list of at most 50 effects")
            return
        for index, effect in enumerate(items):
            here = f"{path}[{index}]"
            if not isinstance(effect, dict) or effect.get("op") not in (
                "set",
                "add",
                "append",
                "remove",
            ):
                self.flag(
                    here,
                    'write {"op": "set", "add", "append" or "remove", "key": state_key, "value": value}',
                )
                continue
            if self.state is None:
                continue
            key, op, value = effect.get("key"), effect["op"], effect.get("value")
            if not isinstance(key, str) or key not in self.state:
                self.flag(f"{here}.key", "name a key declared in state")
                continue
            have = self.state[key]
            if op == "set" and (not _valid_value(value) or _kind(value) != _kind(have)):
                self.flag(
                    here,
                    f"set must match the type of '{key}', which holds {_describe(have)}",
                )
            elif op == "add" and (
                _kind(have) != "number"
                or _kind(value) != "number"
                or not math.isfinite(value)
            ):
                self.flag(
                    here,
                    f"add needs a number key and a number value, and '{key}' holds {_describe(have)}",
                )
            elif op in ("append", "remove") and (
                _kind(have) != "list" or not isinstance(value, str) or len(value) > 1000
            ):
                self.flag(
                    here,
                    f"{op} needs a list key and a text value, and '{key}' holds {_describe(have)}",
                )

    def endings(self, items):
        if not isinstance(items, list) or len(items) > 50:
            self.flag(
                "endings",
                "declare a list of at most 50 endings, or [] for open-ended play",
            )
            return
        seen = set()
        for index, ending in enumerate(items):
            here = f"endings[{index}]"
            if not isinstance(ending, dict):
                self.flag(
                    here,
                    "write each ending as an object with id, label, text, status, terminal and when",
                )
                continue
            ending_id = ending.get("id")
            if not _valid_id(ending_id):
                self.flag(f"{here}.id", ID_RULE)
            elif ending_id in seen:
                self.flag(f"{here}.id", f"'{ending_id}' repeats")
            else:
                seen.add(ending_id)
            if not _text(ending.get("label"), 160):
                self.flag(f"{here}.label", "write a label of 1 to 160 characters")
            if not _text(ending.get("text")):
                self.flag(f"{here}.text", "write the ending text")
            if ending.get("status") not in ("complete", "failed"):
                self.flag(f"{here}.status", 'use "complete" or "failed"')
            if not isinstance(ending.get("terminal"), bool):
                self.flag(
                    f"{here}.terminal",
                    "use true to end play here or false to continue after it",
                )
            if "when" not in ending:
                self.flag(
                    f"{here}.when", "write the condition that triggers this ending"
                )
            else:
                self.condition(ending["when"], f"{here}.when")

    def sources(self, items):
        if not isinstance(items, list) or len(items) > 50:
            self.flag("sources", "list at most 50 sources")
            return
        for index, source in enumerate(items):
            here = f"sources[{index}]"
            if (
                not isinstance(source, dict)
                or not _text(source.get("id"), 160)
                or not _text(source.get("text"), 30000)
            ):
                self.flag(
                    here,
                    "write each source with an id of 1 to 160 characters and its text",
                )
            elif source.get("url") and not re.match(r"https?://", str(source["url"])):
                self.flag(f"{here}.url", "use an http or https address")


# ---------- non-blocking notes for the participant ----------


def _holds(cond, state):
    op, arg = next(iter(cond.items()))
    if op == "all":
        return all(_holds(c, state) for c in arg)
    if op == "any":
        return any(_holds(c, state) for c in arg)
    if op == "not":
        return not _holds(arg, state)
    have, want = state[arg[0]], arg[1]
    return {
        "eq": lambda: have == want,
        "ne": lambda: have != want,
        "gt": lambda: have > want,
        "gte": lambda: have >= want,
        "lt": lambda: have < want,
        "lte": lambda: have <= want,
        "includes": lambda: want in have,
    }[op]()


def _warnings(s):
    notes = []
    pending = [s["start"]] + [
        c["to"] for c in s.get("global_choices", []) if c.get("to")
    ]
    reached = set()
    while pending:
        node_id = pending.pop()
        if node_id not in reached:
            reached.add(node_id)
            pending += [c["to"] for c in s["nodes"][node_id]["choices"] if c.get("to")]
    unreached = [n for n in s["nodes"] if n not in reached]
    if unreached:
        notes.append("No choice leads to node " + ", ".join(unreached[:10]) + ".")
    for ending in s["endings"]:
        if _holds(ending["when"], s["state"]):
            notes.append(
                f"Ending '{ending['id']}' already holds at the start, so play opens on it."
            )
            break
    return notes


def _theme(value):
    name = str(value or "").strip().lower().replace(" ", "-").replace("_", "-")
    return name if name in THEMES else THEMES[0]


def _speed(value):
    if isinstance(value, str):
        word = value.strip().lower()
        if word in SPEEDS:
            return SPEEDS[word]
        try:
            value = float(word)
        except ValueError:
            return 75
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        return 75
    return min(SPEEDS.values(), key=lambda option: abs(option - value))


class Tools:
    def render_adventure(
        self, scenario_json: str = "", theme: str = "cuny-blue", text_speed: int = 75
    ):
        """
        Render the participant's own choice adventure in an embedded player, never a default story.
        Draft the scenario from the participant's material. Before the call, ask for any missing topic, choices, and intended ending or open-ended preference, and confirm inferred rules with the participant. Do not invent source claims.
        If the result lists errors, fix only those paths and call again with the same content. Model prose never changes game state, so judge progress or completion only from the Play record the participant copies.
        :param scenario_json: Adventure JSON with schema_version 2. Required keys are title, introduction, start (first node id), nodes (object keyed by node id) and endings ([] for open-ended play). Optional keys are state (object of true/false, number, text or list-of-text values), objective, global_choices and sources [{id, text, url}]. Node = {name, text, choices}. Choice = {id (unique), label, text (result), to (node id), when (condition), effects, blocked_text, hidden}. A visible choice whose condition fails shows blocked_text and changes nothing; a hidden choice appears only while its condition holds. Condition = {"all": [...]}, {"any": [...]}, {"not": {...}} or {"eq"|"ne"|"gt"|"gte"|"lt"|"lte"|"includes": [state_key, value]}. Effect = {"op": "set"|"add"|"append"|"remove", "key": state_key, "value": value}. Ending = {id, label, text, status "complete" or "failed", terminal true or false, when}. Ids start with a letter and use letters, digits, _ or -.
        :param theme: Optional look, one of cuny-blue, linux-terminal, classic-arcade or bauhaus. Other values fall back to cuny-blue.
        :param text_speed: Optional characters per second, 0 (instant), 35, 75 or 140. Other values snap to the nearest option.
        """
        scenario, problem = _parse(scenario_json)
        if problem is None:
            problem = _normalize(scenario)
        if problem is not None:
            return problem
        errors = _Checker(scenario).run()
        if errors:
            return {
                "status": "invalid_input",
                "message": "The player did not render. Fix these paths and call render_adventure again with the same content. Ask the participant before changing story facts or rules.",
                "errors": errors,
            }
        payload = json.dumps(
            {
                "scenario": scenario,
                "theme": _theme(theme),
                "text_speed": _speed(text_speed),
            },
            ensure_ascii=True,
            allow_nan=False,
        )
        payload = (
            payload.replace("<", "\\u003c")
            .replace(">", "\\u003e")
            .replace("&", "\\u0026")
        )
        context = {
            "status": "render_requested",
            "title": scenario["title"],
            "schema_version": 2,
            "size": {
                "nodes": len(scenario["nodes"]),
                "choices": sum(len(n["choices"]) for n in scenario["nodes"].values())
                + len(scenario.get("global_choices", [])),
                "endings": len(scenario["endings"]),
                "state_keys": len(scenario["state"]),
            },
            "validation": "Every rule and reference passed before rendering. Confirm with the participant that the player appears.",
            "evidence": "Choices happen inside the embedded player. Ask the participant to copy the Play record before judging progress or completion. Sources are supplied material, not independently verified.",
            "persistence": "Session-only. Undo replays earlier choices, Restart begins a new run, and Stop halts without claiming completion.",
        }
        warnings = _warnings(scenario)
        if warnings:
            context["warnings"] = warnings
        page = HTML_TEMPLATE.replace("/*PAYLOAD*/", payload, 1)
        return (
            HTMLResponse(content=page, headers={"Content-Disposition": "inline"}),
            context,
        )


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Adventure</title>
<style>
:root{color-scheme:light;--bg:#fff;--text:#011d49;--muted:#536582;--accent:#0033a1;--rule:#dce3ef;--band:#0033a1;--band-text:#fff;--band-rule:#ffb71b;--hover:#eff4fc;--danger:#a80400;--font:Arial,Helvetica,sans-serif}
html[data-theme="linux-terminal"]{color-scheme:dark;--bg:#0b100d;--text:#c3efd1;--muted:#91ae99;--accent:#83edac;--rule:#2b4032;--band:#0b100d;--band-text:#83edac;--band-rule:#3d6349;--hover:#172b1e;--danger:#ffa49a;--font:ui-monospace,SFMono-Regular,Consolas,monospace}
html[data-theme="classic-arcade"]{color-scheme:dark;--bg:#050c27;--text:#e8edff;--muted:#acbee8;--accent:#ffe45b;--rule:#1e4262;--band:#050c27;--band-text:#ffe45b;--band-rule:#15cbea;--hover:#14264e;--danger:#ffa0cf;--font:ui-monospace,SFMono-Regular,Consolas,monospace}
html[data-theme="bauhaus"]{--bg:#f5f0e6;--text:#171717;--muted:#59544c;--accent:#0045ad;--rule:#c9c2b8;--band:#f5f0e6;--band-text:#171717;--band-rule:#39342d;--hover:#eae3d6;--danger:#b8221c}
html{scrollbar-gutter:stable}
*{box-sizing:border-box}
[hidden]{display:none!important}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.6 var(--font)}
main{max-width:960px;margin:0 auto;padding:16px 24px 24px}
p{margin:0}
header{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-start;gap:16px 28px;padding:24px;background:var(--band);color:var(--band-text);border-bottom:2px dotted var(--band-rule)}
.heading{flex:1 1 320px;min-width:0}
h1{margin:0;font-size:clamp(28px,4.5vw,44px);line-height:1.1;overflow-wrap:anywhere}
#intro{margin-top:12px;max-width:600px;font-size:14px}
.scene{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;margin:28px 0 14px;padding-bottom:10px;border-bottom:1px dotted var(--rule)}
h2{margin:0;font-size:23px;line-height:1.3;color:var(--accent)}
#moves,#status{font-size:12px;color:var(--muted)}
#status{color:var(--accent);font-weight:700}
#objective{margin-bottom:12px;font-size:13px;color:var(--muted)}
#log{max-width:740px;min-height:3.2em;white-space:pre-wrap;overflow-wrap:anywhere}
button,select{min-height:44px;font:inherit;color:inherit;background:transparent;border:0;border-radius:0;cursor:pointer}
button:disabled{opacity:.4;cursor:default}
select{padding:8px 10px;font-size:13px;color:var(--text);background:var(--bg)}
#choices{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px 24px;margin-top:18px}
#choices button{padding:12px 10px;text-align:left;font-size:16px;line-height:1.5;color:var(--accent);border-bottom:1px dotted var(--rule);overflow-wrap:anywhere}
#choices button:hover{background:var(--hover)}
#skip,.tools button,#copy{padding:0 6px;font-size:13px;color:var(--accent)}
#notice{margin-top:12px;font-size:13px;color:var(--danger);white-space:pre-wrap}
#notice.ok{color:var(--muted)}
#notice:empty{display:none}
footer{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;margin-top:12px;padding-top:10px;font-size:12px;color:var(--muted);border-top:1px dotted var(--rule)}
.tools{display:flex;gap:12px}
.pick{display:flex;align-items:center;gap:8px;font-size:12px}
details{margin-top:18px}
summary{min-height:44px;line-height:44px;cursor:pointer}
label[for="record"]{display:block;margin-bottom:6px;font-size:13px;color:var(--muted)}
pre,textarea{width:100%;margin:0;white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.5 ui-monospace,SFMono-Regular,Consolas,monospace}
textarea{min-height:180px;padding:12px;color:var(--text);background:var(--bg);border:1px solid var(--rule)}
button:focus-visible,select:focus-visible,summary:focus-visible,textarea:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
#location:focus{outline:none}
.sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;border:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap}
@media (max-width:640px){main{padding:12px 14px 20px}header{padding:18px}#choices{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>
<main aria-label="Text adventure">
<header>
<div class="heading"><h1 id="title"></h1><p id="intro"></p></div>
<label class="pick">Theme
<select id="theme">
<option value="cuny-blue">CUNY Blue</option>
<option value="linux-terminal">Linux terminal</option>
<option value="classic-arcade">Classic arcade</option>
<option value="bauhaus">Bauhaus</option>
</select>
</label>
</header>
<section aria-label="Play area">
<div class="scene"><h2 id="location" tabindex="-1"></h2><span id="moves"></span><span id="status" hidden></span></div>
<p id="objective" hidden></p>
<div id="log"></div>
<button id="skip" type="button" hidden>Show all</button>
<div id="choices" role="group" aria-label="Choices"></div>
</section>
<p id="notice" role="status"></p>
<div id="announce" class="sr-only" aria-live="polite"></div>
<footer>
<div class="tools"><button id="undo" type="button">Undo</button><button id="restart" type="button">Restart</button><button id="stop" type="button">Stop</button></div>
<label class="pick">Text speed
<select id="speed"><option value="35">Slow</option><option value="75">Medium</option><option value="140">Fast</option><option value="0">Instant</option></select>
</label>
</footer>
<details><summary>Adventure state</summary><pre id="state"></pre></details>
<details><summary>Play record</summary>
<label for="record">Actual choices and rule results for this run</label>
<textarea id="record" readonly spellcheck="false"></textarea>
<button id="copy" type="button">Copy play record</button>
</details>
</main>
<script id="adventure-data" type="application/json">/*PAYLOAD*/</script>
<script>
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  try {
    var data = JSON.parse($('adventure-data').textContent);
    var s = data.scenario;
    var copy = function (x) { return JSON.parse(JSON.stringify(x)); };
    var state, timer = null, lastHeight = 0;
    var reduced = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    var speed = reduced ? 0 : data.text_speed;

    /* Rules. The server already checked every condition and effect, so these only evaluate. */
    function holds(c, vars) {
      if (c === undefined) return true;
      var op = Object.keys(c)[0], arg = c[op];
      if (op === 'all') return arg.every(function (x) { return holds(x, vars); });
      if (op === 'any') return arg.some(function (x) { return holds(x, vars); });
      if (op === 'not') return !holds(arg, vars);
      var have = vars[arg[0]], want = arg[1];
      if (op === 'eq') return JSON.stringify(have) === JSON.stringify(want);
      if (op === 'ne') return JSON.stringify(have) !== JSON.stringify(want);
      if (op === 'gt') return have > want;
      if (op === 'gte') return have >= want;
      if (op === 'lt') return have < want;
      if (op === 'lte') return have <= want;
      return have.indexOf(want) !== -1;
    }
    function endingFor(vars) {
      for (var i = 0; i < s.endings.length; i++) if (holds(s.endings[i].when, vars)) return s.endings[i];
      return null;
    }
    function begin() {
      var e = endingFor(s.state);
      return { node: s.start, vars: copy(s.state), events: [], status: e ? e.status : 'active', ending: e ? copy(e) : null, stopped: false };
    }
    function available(st) {
      if (st.stopped || (st.ending && st.ending.terminal)) return [];
      return s.nodes[st.node].choices.concat(s.global_choices || []).filter(function (c) { return !c.hidden || holds(c.when, st.vars); });
    }
    function act(old, id) {
      var c = available(old).filter(function (x) { return x.id === id; })[0];
      if (!c) throw new Error('That choice is not available now.');
      if (old.events.length >= 2000) throw new Error('Play record limit reached.');
      var st = copy(old), ok = holds(c.when, st.vars);
      if (ok) {
        (c.effects || []).forEach(function (fx) {
          var v = st.vars[fx.key];
          if (fx.op === 'set') st.vars[fx.key] = copy(fx.value);
          if (fx.op === 'add') {
            st.vars[fx.key] = v + fx.value;
            if (!isFinite(st.vars[fx.key])) throw new Error('Numeric state exceeded its range.');
          }
          if (fx.op === 'append' && v.indexOf(fx.value) === -1) {
            if (v.length >= 200) throw new Error('State list exceeded 200 entries.');
            v.push(fx.value);
          }
          if (fx.op === 'remove') st.vars[fx.key] = v.filter(function (x) { return x !== fx.value; });
        });
        if (c.to) st.node = c.to;
      }
      var e = endingFor(st.vars);
      st.ending = e ? copy(e) : null;
      st.status = e ? e.status : 'active';
      st.events.push({ turn: st.events.length + 1, choice: id, label: c.label, valid: ok, from_node: old.node,
        text: ok ? c.text : (c.blocked_text || 'This choice does not meet its declared conditions.'),
        node: st.node, state: copy(st.vars), status: st.status, ending: e ? e.id : null });
      return st;
    }
    function halt(old) {
      if (old.stopped) return old;
      var st = copy(old);
      st.stopped = true;
      st.status = 'stopped';
      st.events.push({ turn: st.events.length + 1, choice: null, label: 'Stop', valid: true, from_node: old.node,
        text: 'Adventure stopped.', node: st.node, state: copy(st.vars), status: 'stopped', ending: st.ending ? st.ending.id : null });
      return st;
    }
    function replay(ids) {
      var st = begin();
      ids.forEach(function (id) { st = id === null ? halt(st) : act(st, id); });
      return st;
    }

    /* Display. */
    function note(message, ok) {
      $('notice').textContent = message;
      $('notice').className = ok ? 'ok' : '';
    }
    function finish() {
      if (timer !== null) { clearInterval(timer); timer = null; }
      $('log').textContent = $('log').getAttribute('data-full') || '';
      $('log').style.minHeight = '';
      $('skip').hidden = true;
      $('announce').textContent = $('log').textContent;
    }
    function show(message) {
      if (timer !== null) { clearInterval(timer); timer = null; }
      $('log').setAttribute('data-full', message);
      if (!speed) { finish(); return; }
      var chars = Array.from(message), shown = 0, step = Math.max(1, Math.round(speed / 20));
      $('log').textContent = message;
      $('log').style.minHeight = $('log').offsetHeight + 'px';
      $('log').textContent = '';
      $('skip').hidden = false;
      timer = setInterval(function () {
        shown = Math.min(chars.length, shown + step);
        $('log').textContent = chars.slice(0, shown).join('');
        if (shown === chars.length) finish();
      }, 50);
    }
    function render() {
      var node = s.nodes[state.node];
      var last = state.events.length ? state.events[state.events.length - 1] : null;
      $('location').textContent = node.name;
      $('moves').textContent = state.events.length + (state.events.length === 1 ? ' choice' : ' choices');
      $('status').hidden = state.status === 'active';
      $('status').textContent = state.stopped ? 'Stopped' : (state.ending ? state.ending.label : state.status);
      var box = $('choices');
      while (box.firstChild) box.removeChild(box.firstChild);
      available(state).forEach(function (c) {
        var b = document.createElement('button');
        b.type = 'button';
        b.textContent = c.label;
        b.addEventListener('click', function () { choose(c.id); });
        box.appendChild(b);
      });
      $('undo').disabled = state.events.length === 0;
      $('stop').disabled = state.stopped;
      var message = last ? last.text : node.text;
      if (last && last.valid && last.choice !== null && last.node !== last.from_node) message += '\n\n' + node.text;
      if (state.ending && !state.stopped) message += '\n\n' + state.ending.text;
      show(message);
      $('state').textContent = JSON.stringify(state.vars, null, 2);
      $('record').value = JSON.stringify({ schema_version: 2, title: s.title, sources: s.sources || [], node: state.node,
        state: state.vars, status: state.status, ending: state.ending, events: state.events }, null, 2);
      note('');
    }
    function choose(id) {
      try { state = act(state, id); render(); $('location').focus({ preventScroll: true }); }
      catch (err) { note(err.message); }
    }

    /* Open WebUI sizes the embed from these messages, including when text or details expand. */
    function report() {
      var h = Math.ceil(document.body.getBoundingClientRect().height);
      if (window.parent === window || Math.abs(h - lastHeight) < 2) return;
      lastHeight = h;
      window.parent.postMessage({ type: 'iframe:height', height: h }, '*');
    }

    $('undo').addEventListener('click', function () {
      state = replay(state.events.slice(0, -1).map(function (e) { return e.choice; }));
      render();
    });
    $('restart').addEventListener('click', function () { state = begin(); render(); });
    $('stop').addEventListener('click', function () { state = halt(state); render(); finish(); });
    $('skip').addEventListener('click', finish);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') finish(); });
    $('theme').addEventListener('change', function () { document.documentElement.setAttribute('data-theme', $('theme').value); });
    $('speed').addEventListener('change', function () { speed = Number($('speed').value); finish(); });
    $('copy').addEventListener('click', function () {
      var box = $('record'), done = false;
      var manual = function () { note('Press Ctrl+C or Command+C to copy the selected record.'); };
      box.focus();
      box.select();
      try { done = document.execCommand('copy'); } catch (err) { done = false; }
      if (done) { note('Play record copied.', true); return; }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(box.value).then(function () { note('Play record copied.', true); }, manual);
      } else {
        manual();
      }
    });
    if (window.ResizeObserver) new ResizeObserver(report).observe(document.body);
    window.addEventListener('resize', report);
    Array.prototype.forEach.call(document.querySelectorAll('details'), function (d) { d.addEventListener('toggle', report); });

    $('title').textContent = s.title;
    document.title = s.title;
    $('intro').textContent = s.introduction;
    if (s.objective) { $('objective').textContent = s.objective; $('objective').hidden = false; }
    $('theme').value = data.theme;
    document.documentElement.setAttribute('data-theme', data.theme);
    $('speed').value = String(speed);
    window.adventure = {
      snapshot: function () { return JSON.parse($('record').value); },
      run: function (id) { state = act(state, id); render(); },
      stop: function () { state = halt(state); render(); finish(); }
    };
    window.render_game_to_text = function () { return $('record').value; };
    state = begin();
    render();
    report();
  } catch (error) {
    $('title').textContent = 'Adventure could not start';
    $('notice').textContent = String((error && error.message) || error);
  }
})();
</script>
</body>
</html>
"""
