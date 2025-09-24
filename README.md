
# ChatGPT User Prompt Extractor

A Python CLI tool to extract user prompts from ChatGPT conversation JSON exports. Given a ChatGPT JSON file, this script extracts all messages where the **ROLE IS USER**, filters by an optional starting date, and outputs the results in a clean, timestamped text format.


## Features

- Extracts all user prompts from ChatGPT JSON conversation exports.
- Filters prompts starting from an optional specified date.
- Groups extracted prompts by conversation title.
- Supports appending to or creating output files.


## Requirements
- Python 3.7 or higher
- python-dateutil package for robust date parsing

Install dependencies with:
```
pip install python-dateutil
```
## Usage/Examples

Run the script from the command line with:

```python
py run.py <path-to-json-file> <path-to-output-file> [starting-date]
```

- `<path-to-json-file>`: Full path to the ChatGPT JSON export file.
- `<path-to-output-file>`: Path to the text file where extracted data will be saved. The file will be created if it does not exist or appended if it does.
- `[starting-date] (optional)`: Filter prompts from this date forward (format: YYYY-MM-DD). If omitted, all prompts are extracted.

**Examples**
Extract all prompts:
```
py run.py "G:\Users\Git\Source\conversations.json" "G:\Users\Git\Source\gpt-export-json.txt"
```

Extract prompts starting from November 30, 2022
```
py run.py "G:\Users\Git\Source\conversations.json" "G:\Users\Git\Source\gpt-export-json.txt" 2022-11-30
```

**Output Format**
```
[Conversation Title]
YYYY-MM-DD HH:MM:SS - User prompt text
YYYY-MM-DD HH:MM:SS - User prompt text

[Another Conversation Title]
YYYY-MM-DD HH:MM:SS - User prompt text
...

```
## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[MIT](https://choosealicense.com/licenses/mit/)
