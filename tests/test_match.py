#!/usr/bin/env python3

import unittest

# Enables executing this module directly.
# Ref: Remi - https://stackoverflow.com/a/9806045
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
        self.assertFalse(match("a.b|b*", "bbbbbx"))

    def test_concat(self):
        self.assertTrue(match("h.e.l.l.o", "hello"))

    def test_optional(self):
        self.assertTrue(match("a?.b", "b"))
        self.assertTrue(match("a?.b", "ab"))

    def test_alternation(self):
        self.assertTrue(match("a|b", "b"))
        self.assertFalse(match("a|b", "x"))

    def test_group(self):
        self.assertTrue(match("(a.b)*", "ababab"))
        self.assertTrue(match("(a.b)+", "ababab"))

    def test_invalid_group(self):
        self.assertRaises(InvalidRegexError, match, "a|b)", "a")

    def test_invalid_regex(self):
        self.assertRaises(InvalidRegexError, match, ".a|b", "a")

    def test_empty_kleene(self):
        self.assertTrue(match("b*", ""))

    def test_empty_plus(self):
        self.assertFalse(match("b+", ""))


if __name__ == '__main__':
    unittest.main()
