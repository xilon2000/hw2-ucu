from pathlib import Path
import sys


def main():
    if len(sys.argv) > 1:
        print_files(sys.argv[1:])
    else:
        print("No file names were passed.")


def print_files(filenames: list[str]):
    for filename in filenames:
        print_file_content(filename)


def print_file_content(filename: str):
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            content = f.read()
        print(f"File: {filename}")
        print(f"Content:")
        print(content)
    except Exception as e:
        print(f"Error reading file {filename}:")
        print(f"{e}")
        exit(1)


if __name__ == "__main__":
    main()


