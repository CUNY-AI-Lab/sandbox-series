from typing import Any, Optional

MAX_CHARS = 10_000


def _validate_text(value: Any) -> Optional[str]:
    """
    Validate the input for the line-counting tool.

    Args:
        value: The raw argument supplied by the model.

    Returns:
        None if valid, or a short error message explaining the failure.
    """
    if not isinstance(value, str):
        return f"Expected a string, got {type(value).__name__}."
    if len(value) > MAX_CHARS:
        return f"Input is {len(value)} characters; maximum allowed is {MAX_CHARS}."
    return None


def _count_nonblank_lines(text: str) -> int:
    """
    Count lines that contain at least one non-whitespace character.

    Args:
        text: A pre-validated string.

    Returns:
        Number of nonblank lines.
    """
    return sum(1 for line in text.splitlines() if line.strip())


class Tools:
    """
    Open WebUI Tool: counts nonblank lines in user-supplied text.
    """

    def count_nonblank_lines(self, text: str = "") -> dict:
        """
        Count nonblank lines in the provided text.

        Args:
            text: The input string to analyze. Must be a string no longer than
                  10,000 characters.

        Returns:
            On success: {"success": true, "count": <int>, "length": <int>}
            On failure: {"success": false, "error": "<message>"}
        """
        error = _validate_text(text)
        if error:
            return {"success": False, "error": error}

        count = _count_nonblank_lines(text)
        return {
            "success": True,
            "count": count,
            "length": len(text),
        }
