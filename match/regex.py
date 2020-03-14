"""This module provides functions for compiling a regular expression into an
NFA and checking if that NFA matches a given search string.

**Supported Operators**:
    This module supports a limited number of operators, outlined below:

    * ``.`` - Concatenation. Note that this character denotes *explicit*
        concatenation. (e.g. The regex "h.e.l.l.o" is required to match
        the string "hello").

    * ``|`` - The OR operator.

    * ``?`` - Indicates an optional character (zero or one occurrences).

    * Repetitions:
        * ``+`` - The plus symbol indicates one or more occurrences of the
            preceding character.
        * ``*`` - The Kleene star indicates zero or more occurrences of the
            preceding character.

    Unfortunately it is not yet possible to "escape" any of these characters
    in order to match the literal equivalent.
"""

from .shunting_yard import shunt
from .states import (
    EPSILON,
    Fragment,
    State
)


class InvalidRegexError(ValueError):
    """Raised to indicate a string is not a valid regular expression,
    and is therefore unable to be compiled into a NFA.
    """

    # Make this exception always have (an overridable) default message
    # Ref: https://stackoverflow.com/a/56967197
    def __init__(self, msg='Invalid regular expression', *args):
        super().__init__(msg, *args)


def compile_regex(regex: str) -> Fragment:
    """Compiles a given regular expression in infix notation to a NFA Fragment
    and returns it.

    :param regex: The (infix) regular expression to be compiled.
    :return: A :class:`Fragment` that represents the compiled regular
        expression.
    :raises InvalidRegexError: If `regex` is not a valid infix regular expression.
    """

    # Turn the (infix) regular expression into postfix/RPN, since it's easier
    # to turn a postfix expression into a NFA
    try:
        postfix = shunt(regex)
        postfix = list(postfix)[::-1]
    except ValueError as err:
        raise InvalidRegexError from err

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

                # Create new start & accept states
                start = frag2.start
                accept = frag1.accept
            else:
                # Create new start & accept states
                accept = State()
                start = State(edges=[frag2.start, frag1.start])

                # Point the old accept states at the new one
                frag2.accept.edges.append(accept)
                frag1.accept.edges.append(accept)
        elif c in ('*', '+', '?'):
            # If a unary operator is read, there should be at least one
            # Fragment in the `nfa_stack`.
            if len(nfa_stack) == 0:
                raise InvalidRegexError

            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            accept = State()     # New start state

            if c == '*':
                # Create new accept states
                start = State(edges=[frag.start, accept])

                # Point this fragments accept to the new accept states
                frag.accept.edges = [frag.start, accept]
            elif c == '+':
                # Create new accept state
                start = State(edges=[frag.start])

                # Point this fragments accept to the new accept states
                frag.accept.edges = [frag.start, accept]
            else:
                # Create new accept state
                start = State(edges=[frag.start, accept])

                # Point this fragments acceptor to the new acceptor
                frag.accept.edges = [accept]
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # Create new instance of Fragment to represent the new NFA,
        # and push to the NFA stack.
        new_frag = Fragment(start, accept)
        nfa_stack.append(new_frag)

    # `postfix` should be empty & the NFA stack should now only have one NFA on it.
    return nfa_stack.pop()


def match(regex: str, s: str) -> bool:
    """This function will return `True` if the regular expression `regexp`
    (fully) matches the string `s`, and `False` otherwise.

    :param regex: The regular expression to match.
    :param s: The string to check against the regular expression.
    :return: `True` if the string `s` matches the regular expression, and
        `False` otherwise.
    :raises InvalidRegexError: If the regular expression is an empty string.
    """

    if not regex:
        raise InvalidRegexError("regex cannot be an empty string")

    # Compile the regular expression into an NFA & check if it matches `s`.
    nfa = compile_regex(regex)

    current = set()     # The current set of visited states

    # Add the first state and follow all EPSILON arrows
    follow_eps(nfa.start, current)

    for c in s:
        previous = current      # This keeps track of where we were
        # Create a new empty set for states we're about to be in
        current = set()

        for state in previous:
            # Only follow arrows not labeled by EPSILON, and equal to `c`
            if state.label == c and c is not EPSILON:
                # Add the state at the end of the arrow to `current`
                follow_eps(state.edges[0], current)

    return nfa.accept in current


def follow_eps(state: State, current: set):
    """ Adds a state to a set and follows all of the EPSILON (ε) arrows.

    :param state: A state to follow.
    :param current: A `set` of the currently visited states.
    """

    # If `state` is already in `current` there is no need to follow
    if state in current:
        return

    current.add(state)

    if state.label is EPSILON:
        # Loop through the states pointed to by this state & follow
        # all of their EPSILON edges too
        for vertex in state.edges:
            follow_eps(vertex, current)
