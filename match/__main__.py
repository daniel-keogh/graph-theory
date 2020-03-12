""" Main entry-point to the application. """

import sys

from .cli import parse
from .regex import (
    match,
    InvalidRegexpError
)


def main():
    """
    Main entry-point to the application. This function parses the user's
    command line arguments and prints the result to the console.
    """

    args = parse()

    try:
        is_match = match(args.regexp, args.text)
        print(is_match)
    except InvalidRegexpError as err:
        print(f"[Error]: {err}.", file=sys.stderr)
    except Exception as err:
        print(f"[Error]: {type(err).__name__} - {err}.", file=sys.stderr)


if __name__ == "__main__":
    main()
