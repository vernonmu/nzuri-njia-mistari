import pyperclip
import re

def convert_to_markdown(text):
    # Split the text into lines
    lines = text.split('\n')

    # Initialize an empty list to store the converted lines
    markdown_lines = []

    for line in lines:
        # Convert headers (assuming headers are all uppercase)
        if line.strip() and line == line.upper():
            markdown_lines.append('# ' + line)

        # Convert sub-headers (assuming sub-headers are capitalized and followed by a newline)
        elif re.match(r'^[A-Z][a-z]*:', line.strip()):
            markdown_lines.append('## ' + line.strip().replace(':', ''))

        # Convert bold text (assuming bold text is wrapped in ** in plain text)
        elif re.search(r'\*\*(.*?)\*\*', line):
            markdown_lines.append(re.sub(r'\*\*(.*?)\*\*', r'**\1**', line))

        # Convert italics text (assuming italics text is wrapped in * in plain text)
        elif re.search(r'\*(.*?)\*', line):
            markdown_lines.append(re.sub(r'\*(.*?)\*', r'*\1*', line))

        # Convert lists (assuming lists start with "-" or "*" in plain text)
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            markdown_lines.append(line)

        # Leave other lines as they are
        else:
            markdown_lines.append(line)

    # Join the converted lines back into a single string
    return '\n'.join(markdown_lines)

def main():
    # Get the content from the clipboard
    text = pyperclip.paste()

    # Convert plain text to Markdown
    markdown_text = convert_to_markdown(text)

    # Path to the output Markdown file
    output_file_path = 'output.md'
    
    # Write the Markdown text to a new file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_text)

    print(f"Markdown file created: {output_file_path}")

if __name__ == "__main__":
    main()
