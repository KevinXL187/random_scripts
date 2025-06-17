import re

def content_title(lines):
    def sort_key(line):
        match = re.match(r"([a-zA-Z]+)(\s*-\s*\d+)?", line)

        if match:
            letters = match.group(1)
            numbers = match.group(2)
            number = int(numbers.split('-')[1].strip()) if numbers else 0
            return (letters.lower(), number)
        return ("", 0)

    sorted_lines = sorted(lines, key=sort_key)
    return sorted_lines

def file_edit(input, output):
    with open(input) as f:
        pass

if __name__ == "__main__":
    content_title()