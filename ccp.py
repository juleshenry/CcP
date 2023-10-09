import argparse

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

if __name__ == "__main__":
    args = parse_arguments()

    print(f"File: {args.file}")
    print(f"Lines: {args.lines}")
    print(f"Adjustments: {args.adjustments}")
