"""
This package allows you to check if a regular expression matches a given
string of text, using an algorithm known as Thompson's construction.

Thompson's Construction Summary
===============================
Thompson's construction is a method of transforming a regular expression into
a non-deterministic finite automaton (NFA). Like regular expressions, NFAs
are a way of describing sets of character strings, and every valid regular
expression will have an equivalent NFA that matches the same set of strings.

Thompson's algorithm works by building small NFA fragments that represent
part of a regular expression, and then composing larger NFAs from those
smaller NFA fragments, with a different construction for each operator.

Performance
-----------
The algorithm offers a significant performance boost over the more
complex, real-world regular expression implementations used in programming
languages like Perl, Python, and others.

References & Further Info
=========================
    *   Cox, Russ - `Regular Expression Matching Can Be Simple And Fast
        <https://swtch.com/~rsc/regexp/regexp1.html>`_
"""

__author__ = "Daniel Keogh"
__license__ = "MIT"
__version__ = "1.0.0"
