import sys

import requests


def main():

    if len(sys.argv) <= 1:
        print("No url was passed.")
    else:
        url = sys.argv[1]
        r = requests.get(url)
        print(r.text)


if __name__ == "__main__":
    main()
