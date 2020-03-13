#!/usr/bin/env python3

import unittest

# Allow executing this module directly: https://stackoverflow.com/a/9806045
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from match.shunting_yard import shunt


class ShuntingTest(unittest.TestCase):
    def test_shunting(self):
        self.assertEqual(shunt("(a|b).c*"), "ab|c*.")

    def test_unbalanced_parens(self):
        self.assertRaises(ValueError, shunt, "(a|b)))")


if __name__ == '__main__':
    unittest.main()
