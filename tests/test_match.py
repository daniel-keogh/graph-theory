#!/usr/bin/env python3

import unittest

# Allow executing this module directly: https://stackoverflow.com/a/9806045
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from match.regex import (
    match,
    InvalidRegexError
)


class MatchTest(unittest.TestCase):
    def test_match(self):
        self.assertTrue(match("a.b|b*", "bbbbbbb"))

    def test_false(self):
        self.assertFalse(match("a.b|b*", "bbx"))

    def test_concat(self):
        self.assertTrue(match("a.b", "ab"))

    def test_group(self):
        self.assertTrue(match("(a.b)*", "ababab"))

    def test_invalid_re(self):
        self.assertRaises(InvalidRegexError, match, ".a|b", "a")

    def test_empty(self):
        self.assertTrue(match("b*", ""))


if __name__ == '__main__':
    unittest.main()
