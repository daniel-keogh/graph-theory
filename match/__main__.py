#!/usr/bin/env python3

from .cli import parse
from .regex import match


def main():
    args = parse()

    is_match = match(args.regexp, args.text)
    print(is_match)


if __name__ == "__main__":
    main()
