import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description="CSS Parser")
    parser.add_argument("--file", required=True, help="Input CSS file")
    parser.add_argument("--lines", type=str, help="Lines to modify (comma-separated)")
    parser.add_argument(
        "--adjustments",
        type=str,
        required=True,
        help="Adjustments for corresponding lines (comma-separated)",
    )
    parser.add_argument(
        "--regex",
        type=str,
        help="Optional regex that overrides line numbers",
    )
    args = parser.parse_args()

    # Convert lines and adjustments to lists of integers
    if args.lines:
        args.lines = list(map(float, args.lines.split(",")))
    args.adjustments = list(map(float, args.adjustments.split(",")))

    return args


def scalar_array_adjustments(content, lines_to_edit, adjustments):
    """Simple case, scalar or list of scalars"""
    scalar_array_pattern = r"\d+(?:\s+\d+)*(?:\w+)?"
    for line_number, adjustment in zip(lines_to_edit, adjustments):
        text = content[line_number - 1]
        matches = re.findall(scalar_array_pattern, text)
        for match in matches:
            # This applies to the corner-case of padding: 20 20 20 20px and others...
            numbers_in_line = re.findall(r"\d+", match)
            units = re.findall(r"\D+", match)
            # if without units...
            if len(units) != len(numbers_in_line):
                units = [""] * len(numbers_in_line)
            adj_numbs = [
                str(float(num) + adjustment) + unit
                for num, unit in zip(numbers_in_line, units)
            ]
            new_numbers = " ".join(map(str, adj_numbs))

            text = text.replace(match, new_numbers)
        content[line_number - 1] = text
    return content


def regex_adjustments(content, regex, adjustments):
    if len(adjustments) != 1:
        raise ValueError("Only singular scalar supported")
    adjustment = adjustments[0]
    # scalar_array_pattern = r"\d+(?:\s+\d+)*(?:\w+)?"
    matcher = re.compile(regex)
    for ix, match in enumerate(content):
        if matcher.search(match):
            # This applies to the corner-case of padding: 20 20 20 20px and others...
            numbers = list(map(float, re.findall(r":\s*([0-9]*\.[0-9]+)", match)))
            alpha = re.findall(r"[^\d.]+", match)
            numb_str = str(numbers[0])
            # Written-out floats in CSS vs. Pythonic float
            if numb_str not in match and numb_str.startswith("0."):
                numb_str = numb_str[1:]
            done = match.replace(numb_str, str(numbers[0] + adjustment))
            content[ix] = done
    return content


def edit_file(file_path, lines_to_edit, adjustments, regex=None):
    # star-map case
    if lines_to_edit and len(adjustments) != len(lines_to_edit):
        adjustments = adjustments * len(lines_to_edit)

    with open(file_path, "r") as file:
        content = file.readlines()
    if not regex:
        content = scalar_array_adjustments(content, lines_to_edit, adjustments)
    else:
        content = regex_adjustments(content, regex, adjustments)
    # Write the modified content back to the file
    with open(file_path.replace(".css", "_new.css"), "w") as file:
        file.writelines(content)


if __name__ == "__main__":
    args = parse_arguments()
    print(f"File: {args.file}")
    print(f"Lines: {args.lines}")
    print(f"Adjustments: {args.adjustments}")
    print(f"Regex: {args.regex}")
    print("$" * 44)
    edit_file(args.file, args.lines, args.adjustments, regex=args.regex)
