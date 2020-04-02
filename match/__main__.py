""" Main entry-point to the program. """

import sys

from .cli import parse
from .regex import match


def main():
    """
    Main entry-point to the program. This function parses the user's command
    line arguments and prints the result of the ``match()`` function to the
    console (either `True` or `False`).
    """

    try:
        args = parse()

        is_match = match(args.regex, args.text)
        print(is_match)
    except Exception as err:
        # Print catch-all error message
        print(f"[{type(err).__name__}]: {err}.", file=sys.stderr)


if __name__ == "__main__":
    main()
