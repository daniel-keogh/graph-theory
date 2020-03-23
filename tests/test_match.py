#!/usr/bin/env python3

import unittest

# The following enables executing this module directly.
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

    def test_mismatch(self):
        self.assertFalse(match("a.b|b*", "bbx"))

    def test_concat(self):
        self.assertTrue(match("h.e.l.l.o", "hello"))

    def test_plus(self):
        self.assertTrue(match("(a.b)+", "abab"))

    def test_optional(self):
        self.assertTrue(match("a?.b", "b"))

    def test_group(self):
        self.assertTrue(match("(a.b)*", "ababab"))

    def test_invalid_regex(self):
        self.assertRaises(InvalidRegexError, match, ".a|b", "a")

    def test_empty_kleene(self):
        self.assertTrue(match("b*", ""))

    def test_empty_plus(self):
        self.assertFalse(match("b+", ""))


if __name__ == '__main__':
    unittest.main()
