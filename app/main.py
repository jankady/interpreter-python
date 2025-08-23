import sys

from .Scanner import Scanner as scan


def main():

    filename = codecrafters()

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)
    tokenize = scan(filename)
    tokenize.tokenize()

def codecrafters():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]
    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)
    return filename

if __name__ == "__main__":
    main()
