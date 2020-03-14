""" Main entry-point to the application. """

import sys

from .cli import parse
from .regex import (
    match,
    InvalidRegexError
)


def main():
    """Main entry-point to the application. This function parses
    the user's command line arguments and prints the result of ``match()``
    to the console.
    """

    try:
        args = parse()

        is_match = match(args.regex, args.text)
        print(is_match)
    except InvalidRegexError as err:
        print(f"[Error]: {err}.", file=sys.stderr)
    except Exception as err:
        # Print catch-all error message
        print(f"[Error]: {type(err).__name__} - {err}.", file=sys.stderr)


if __name__ == "__main__":
    main()
