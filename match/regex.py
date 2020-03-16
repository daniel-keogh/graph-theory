"""
This module provides functions for compiling a regular expression into an
NFA and checking if that NFA matches a given search string.

Supported Operators
===================
    This operators supported by this module are outlined below:

    * ``.`` - Concatenation. Note that this character denotes *explicit*
        concatenation. (e.g. The regular expression "h.e.l.l.o" is required
        in order to match the string "hello").

    * ``|`` - The OR operator represents alternation/union.

    * ``?`` - Indicates an optional character (zero or one occurrences).

    * ``+`` - The plus symbol indicates one or more occurrences of the
        preceding character.

    * ``*`` - The Kleene star indicates zero or more occurrences of the
        preceding character.
"""

from .shunting_yard import shunt
from .states import (
    EPSILON,
    Fragment,
    State
)


class InvalidRegexError(ValueError):
    """
    Raised to indicate a string is not a valid regular expression,
    and is therefore unable to be compiled into a NFA.
    """

    # Make this exception always have (an overridable) default message
    # Ref: https://stackoverflow.com/a/56967197
    def __init__(self, msg='Invalid regular expression', *args):
        super().__init__(msg, *args)


def compile_regex(regex: str) -> Fragment:
    """
    Compiles a given regular expression (in infix notation) to a NFA
    Fragment and returns it.

    :param regex: The regular expression to be compiled.
    :return: A :class:`Fragment` that represents the compiled regular
        expression.
    :raises InvalidRegexError: If `regex` is not a valid infix regular
        expression.
    """

    # Turn the (infix) regular expression into postfix/RPN, since it's easier
    # to turn a postfix expression into a NFA.
    try:
        postfix = shunt(regex)
        postfix = list(postfix)[::-1]
    except ValueError as err:
        raise InvalidRegexError("Unbalanced parentheses") from err

    nfa_stack = []

    while postfix:
        c = postfix.pop()

        if c in ('.', '|'):
            # If a binary operator is read, there should be at least two
            # Fragments in the `nfa_stack`.
            if len(nfa_stack) < 2:
                raise InvalidRegexError

            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            if c == '.':
                # Point frag2's accept state at frag1's start state
                frag2.accept.edges.append(frag1.start)

                # frag2's start state is the new start state & frag1's
                # accept state is the new accept state.
                start = frag2.start
                accept = frag1.accept
            else:
                # Create new start & accept states, with the new start
                # state pointing to the start state of each fragments.
                accept = State()
                start = State(edges=[frag2.start, frag1.start])

                # Point the old accept states at the new one.
                frag2.accept.edges.append(accept)
                frag1.accept.edges.append(accept)
        elif c in ('*', '+', '?'):
            # If a unary operator is read, there should be at least one
            # Fragment in the `nfa_stack`.
            if len(nfa_stack) < 1:
                raise InvalidRegexError

            frag = nfa_stack.pop()    # Pop a single fragment off the stack

            accept = State()          # New accept state

            if c == '*':
                # Create new accept state which points to both the old start
                # state and the new accept state.
                start = State(edges=[frag.start, accept])

                # Point the old fragment's accept to the new accept state.
                frag.accept.edges = [frag.start, accept]
            elif c == '+':
                # Create new accept state which points to the old start state.
                start = State(edges=[frag.start])

                # Point the old fragment's accept to the new accept state.
                frag.accept.edges = [frag.start, accept]
            else:
                # Create the new start state which points to both the old
                # start state and the new accept state.
                start = State(edges=[frag.start, accept])

                # Point the old fragment's acceptor to the new accept state.
                frag.accept.edges = [accept]
        else:
            # For normal characters, make a new accept state, assign a label,
            # and then point the start state to the accept state.
            accept = State()
            start = State(label=c, edges=[accept])

        # Push the new Fragment to the NFA stack.
        new_frag = Fragment(start, accept)
        nfa_stack.append(new_frag)

    # `postfix` should be empty & NFA stack should only have one item on it.
    return nfa_stack.pop()


def match(regex: str, s: str) -> bool:
    """
    This function will return `True` if the regular expression `regexp`
    (fully) matches the string `s`, and `False` otherwise.

    :param regex: The regular expression to match.
    :param s: The string to check against the regular expression.
    :return: `True` if the string `s` matches the regular expression, and
        `False` otherwise.
    :raises InvalidRegexError: If there is an error compiling the regular
        expresion.
    :raises ValueError: If the regular expression is an empty string.
    """

    if not regex:
        raise ValueError("`regex` cannot be an empty string")

    current = set()     # The current set of visited states

    # Compile the regular expression into an NFA
    nfa = compile_regex(regex)

    # Add the first state and follow all arrows labelled with the empty string
    _follow_eps(nfa.start, current)

    for c in s:
        previous = current     # This keeps track of where we were
        # Create empty set for states we're about to be in
        current = set()

        for state in previous:
            # Only follow arrows labeled by `c`, where c != EPSILON
            if state.label == c and c is not EPSILON:
                # Add the state at the end of the arrow to `current`
                _follow_eps(state.edges[0], current)

    return nfa.accept in current


def _follow_eps(state: State, current: set):
    """
    Adds a state to a set and follows all of the edges labelled by
    EPSILON (ε).

    :param state: A state to follow.
    :param current: A `set` of the currently visited states.
    """

    # If `state` is already in `current` there is no need to follow
    if state in current:
        return

    current.add(state)

    if state.label is EPSILON:
        # Loop through the states pointed to by this state & follow
        # all their EPSILON-labelled edges too
        for vertex in state.edges:
            _follow_eps(vertex, current)
