def validate_scenario(s):
    """Reject malformed scenarios before producing an iframe."""
    import re
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    def text(value, limit=3000):
        return isinstance(value, str) and 0 < len(value.strip()) <= limit
    require(isinstance(s, dict), "Scenario must be an object.")
    for field in ("title", "introduction", "start"):
        require(text(s.get(field)), "Invalid " + field)
    rooms = s.get("rooms")
    require(isinstance(rooms, dict) and 2 <= len(rooms) <= 12, "Use 2–12 rooms.")
    require(s["start"] in rooms, "Start room is missing.")
    items = set()
    for identifier, room in rooms.items():
        require(re.fullmatch(r"[a-z][a-z0-9_-]{0,39}", identifier), "Invalid room ID.")
        require(isinstance(room, dict), "Invalid room.")
        require(text(room.get("name"), 100) and text(room.get("description")), "Invalid room text.")
        exits = room.get("exits")
        require(isinstance(exits, dict), "Invalid exits.")
        for direction, target in exits.items():
            require(direction in ("north", "south", "east", "west", "up", "down") and isinstance(target,str) and target in rooms, "Invalid exit.")
        found = room.get("items")
        require(isinstance(found, list) and len(found) <= 12, "Invalid items.")
        for item in found:
            require(isinstance(item, str) and re.fullmatch(r"[a-z][a-z -]{0,39}", item) and item not in items, "Invalid or duplicate item.")
            items.add(item)
    actions = s.get("actions")
    require(isinstance(actions, list) and 1 <= len(actions) <= 30, "Use 1–30 actions.")
    commands, flags = set(), set()
    for action in actions:
        require(isinstance(action, dict), "Invalid action.")
        command = action.get("command")
        require(isinstance(command, str) and re.fullmatch(r"[a-z][a-z -]{1,59}", command) and not re.match(r"^(go |take |look$|inventory$|help$|undo$|restart$|save$|load$|discuss$)", command) and command not in commands, "Invalid or duplicate command.")
        commands.add(command)
        require(isinstance(action.get("room"), str) and action["room"] in rooms and text(action.get("text")), "Invalid action text or room.")
        for field in ("requires_items", "requires_flags", "sets_flags", "clears_flags"):
            value = action.get(field)
            require(isinstance(value, list) and len(value) <= 20 and all(isinstance(x, str) and re.fullmatch(r"[a-z][a-z0-9_ -]{0,39}", x) for x in value), "Invalid condition.")
        require(all(x in items for x in action["requires_items"]), "Unknown required item.")
        flags.update(action["sets_flags"])
    goals = s.get("goal_flags")
    require(isinstance(goals, list) and 0 < len(goals) <= 20 and all(isinstance(x,str) and x in flags for x in goals), "Invalid goal flags.")
    for action in actions:
        require(all(x in flags for x in action["requires_flags"] + action["clears_flags"]), "Unknown flag condition.")
    seen, queue = {s["start"]}, [s["start"]]
    while queue:
        for target in rooms[queue.pop(0)]["exits"].values():
            if target not in seen:
                seen.add(target)
                queue.append(target)
    require(len(seen) == len(rooms), "Every room must be reachable.")
    return s
