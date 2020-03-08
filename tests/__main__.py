#!/usr/bin/env python3

# Allow executing this module directly: https://stackoverflow.com/a/9806045
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from match.regex import match


if __name__ == '__main__':
    tests = [
        ["a.b|b*", "bbbbbbb", True],
        ["a.b|b*", "bbx", False],
        ["a.b", "ab", True],
        ["b*", "", True]
    ]

    for i, test in enumerate(tests):
        try:
            assert match(test[0], test[1]) == test[2], \
                f"{test[0]} {'should' if test[2] else 'should not'} match {test[1]}"
        except AssertionError as err:
            print(f"Test no. {i + 1} Failed: {err}\n", file=sys.stderr)
        else:
            print(f"Test no. {i + 1} Passed.")
