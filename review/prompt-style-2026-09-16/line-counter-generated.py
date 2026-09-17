import json
import re


def _count_non_whitespace_lines(text: str) -> int:
    """Internal helper: count lines with non-whitespace characters."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) > 10000:
        raise ValueError("Input exceeds maximum allowed length of 10,000 characters")
    # Split into lines and count those with at least one non-whitespace char
    return sum(1 for line in text.splitlines() if re.search(r'\S', line))


class Tools:
    def count_non_whitespace_lines(self, text: str) -> dict:
        """
        Count lines containing non-whitespace characters in the given text.

        Parameters:
        - text (str): Input text string to analyze.

        Returns:
        - dict: {"count": integer} where integer is the number of non-blank lines.

        Raises:
        - TypeError: If input is not a string.
        - ValueError: If input length exceeds 10,000 characters.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        if len(text) > 10000:
            raise ValueError("Input exceeds maximum allowed length of 10,000 characters")
        count = _count_non_whitespace_lines(text)
        return {"count": count}
