import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description="CSS Parser")
    parser.add_argument("--file", required=True, help="Input CSS file")
    parser.add_argument("--lines", type=str, required=True, help="Lines to modify (comma-separated)")
    parser.add_argument("--adjustments", type=str, required=True, help="Adjustments for corresponding lines (comma-separated)")

    args = parser.parse_args()

    # Convert lines and adjustments to lists of integers
    args.lines = list(map(int, args.lines.split(',')))
    args.adjustments = list(map(int, args.adjustments.split(',')))

    return args

def edit_file(file_path, lines_to_edit, adjustments):
    if len(adjustments)!=len(lines_to_edit):
        adjustments = adjustments * len(lines_to_edit)
    with open(file_path, 'r') as file:
        content = file.readlines()
    pattern = r'\d+(?:\s+\d+)*(?:\w+)?'
    for line_number, adjustment in zip(lines_to_edit, adjustments):
        text  = content[line_number - 1]
        matches = re.findall(pattern, text)
        for match in matches:
            numbers = [int(num) + adjustment for num in re.findall(r'\d+', match)]
            new_numbers = ' '.join(map(str, numbers))
            text = text.replace(match, new_numbers)
        content[line_number - 1] = text
    # Write the modified content back to the file
    with open(file_path.replace('.css','_new.css'), 'w') as file:
        file.writelines(content)

if __name__ == "__main__":
    args = parse_arguments()
    print(f"File: {args.file}")
    print(f"Lines: {args.lines}")
    print(f"Adjustments: {args.adjustments}")
    edit_file(args.file, args.lines, args.adjustments)