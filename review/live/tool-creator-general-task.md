### Line Counter Tool

**Tool Name:** Line Counter
**Tool ID:** `line_counter`
**Tool Description:** Counts the number of lines in a text string that contain non-whitespace characters. Limits input to 10,000 characters.

#### Python Code

```python
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
```

#### Installation Steps

1.  Open your Open WebUI interface.
2.  Navigate to **Workspace** > **Tools**.
3.  Click **Create**.
4.  Enter **Line Counter** as the Name and `line_counter` as the ID.
5.  Enter the **Description** provided above.
6.  Paste the Python code into the **Code** section.
7.  Click **Save & Create**.
8.  To use it, go to **Integrations** > **Tools** in your chat settings or attach it to a specific model in the Workspace.

#### Proposed Tests

| Test Case | Input | Expected Result |
| :--- | :--- | :--- |
| **Standard Input** | `"Line 1\n\nLine 3\n   \nLine 5"` | `{"non_empty_lines": 3}` |
| **Length Boundary** | `"a" * 10001` | `ValueError: Input text exceeds maximum length...` |
| **Type Validation** | `12345` (Integer) | `TypeError: Input must be a string, received int` |
