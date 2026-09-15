import json

class Tools:
    def count_non_empty_lines(self, text: str) -> dict:
        """
        Counts the number of lines in the provided text that are not empty or purely whitespace.

        Args:
            text (str): The input text to analyze. Must be a string and at most 10,000 characters.

        Returns:
            dict: A dictionary containing the count of non-empty lines, e.g., {"non_empty_lines": 5}.

        Raises:
            TypeError: If the input is not a string.
            ValueError: If the input string exceeds 10,000 characters.
        """
        # Validate input type
        if not isinstance(text, str):
            raise TypeError(f"Input must be a string, received {type(text).__name__}")

        # Validate input length
        if len(text) > 10000:
            raise ValueError(f"Input text exceeds maximum length of 10,000 characters (length: {len(text)})")

        # Split lines and count those that contain characters other than whitespace
        lines = text.splitlines()
        non_empty_count = sum(1 for line in lines if line.strip())

        return {"non_empty_lines": non_empty_count}
