"""
This package allows you to check if a regular expression matches a given string
of text, using an algorithm known as Thompson’s construction.

Thompson's construction is a method of transforming a regular expression into
an equivalent non-deterministic finite automaton (NFA). The algorithm works
by composing small NFA fragments that represent part of the regular expression,
and then building larger NFAs from those smaller NFA fragments.

Thompson's construction offers a significant performance boost over other
traditional backtracking approaches to regular expression matching
(i.e. those used in programming languages like Perl). Such backtracking
algorithms keep track of only one transition at a time, and backtrack
to another path if the current path fails. Thompson's algorithm meanwhile,
tracks all possible transitions simultaneously.

**References**:
    Cox, Russ - `Regular Expression Matching Can Be Simple And Fast
    <https://swtch.com/~rsc/regexp/regexp1.html>`_

    Xiayun Sun - `Regex parsing: Thompson's algorithm
    <https://xysun.github.io/posts/regex-parsing-thompsons-algorithm.html>`_
"""
