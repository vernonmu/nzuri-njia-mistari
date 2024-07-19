# Clipboard to Markdown Converter

This repository contains a Python script that converts rich text copied from the clipboard into Markdown format. The script reads text from the clipboard, applies formatting rules, and outputs the result to a Markdown file.

## Features

- Converts uppercase lines to Markdown headers (`# Header`)
- Converts capitalized lines ending with a colon to sub-headers (`## Sub-header`)
- Preserves bold text wrapped in `**` (e.g., `**bold text**`)
- Preserves italic text wrapped in `*` (e.g., `*italic text*`)
- Converts lists that start with `-` or `*` into Markdown lists
- Leaves other lines unchanged

## Requirements

- Python 3.x
- `pyperclip` library

## Installation

1. Clone the repository:

```
  git clone https://github.com/vernonmu/nzuri-njia-mistari.git
  cd nzuri-njia-mistari
```

2. Install the required library:

```
  pip install pyperclip
```

3. Usage

- Copy the rich text you want to convert to Markdown to your clipboard.
- Run the script:

```
  python main.py
```

- The script will create a file named output.md in the same directory with the converted Markdown content.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or want to add new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
