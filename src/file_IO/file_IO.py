import sys
import json

def read_cmd_filename():
    if len(sys.argv) < 2:
        print("No filename provided. Usage: eva-processor <filename>", file=sys.stderr)
        exit(1)

    # argv[0] is the path to the current executable
    return sys.argv[1]

def load_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} does not exist", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: File {filename} is not valid JSON ({e})", file=sys.stderr)
        sys.exit(1)

    return data
