#!/usr/bin/env python3

import unittest

# Allow executing this module directly: https://stackoverflow.com/a/9806045
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from match.regex import match
from match.shunting import shunting


class MatchTest(unittest.TestCase):
    def test_match(self):
        self.assertTrue(match("a.b|b*", "bbbbbbb"))

    def test_fail(self):
        self.assertFalse(match("a.b|b*", "bbx"))

    def test_concat(self):
        self.assertTrue(match("b*", ""))

    def test_empty(self):
        self.assertTrue(match("b*", ""))


class ShuntingTest(unittest.TestCase):
    def test_shunting(self):
        self.assertEqual(shunting("(a|b).c*"), "ab|c*.")

    def test_parens(self):
        self.assertRaises(ValueError, shunting, "(a|b)))")


if __name__ == '__main__':
    unittest.main()
