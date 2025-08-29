# File Reader and Modifier

This Python program reads the contents of a text file provided by the user, modifies the content (by converting all text to uppercase in this example), and saves the modified content into a new file. The new file will have the same name as the original but with a `modified_` prefix.

---

## Features
- Prompts the user to enter the filename of an existing text file.
- Reads the file content safely.
- Converts the content to **uppercase**.
- Writes the modified content into a new file: `modified_<filename>`.
- Handles common errors such as:
  - File not found
  - File read/write issues

---

## Requirements
- Python 3.x installed on your system.

---

## Usage

1. Save the program into a file, e.g., `file_modifier.py`.
2. Run the script in a terminal or command prompt:
   ```bash
   python file_modifier.py
