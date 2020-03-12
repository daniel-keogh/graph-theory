from .shunting import shunting
from .state import (
    EPSILON,
    Fragment,
    State
)


class InvalidRegexpError(Exception):
    """
    Raised to indicate a string is not a valid regular expression, and is
    therefore unable to be compiled into a NFA.
    """
    pass


def compile_regex(infix: str) -> Fragment:
    """
    Compiles a given regular expression `infix` to a NFA Fragment
    and returns it.
    """

    postfix: str
    try:
        postfix = shunting(infix)
        postfix = list(postfix)[::-1]
    except ValueError:
        raise InvalidRegexpError("Invalid regular expression")

    nfa_stack = []
    newfrag: Fragment = None

    while postfix:
        c = postfix.pop()       # Pop a character from postfix

        if c == '.':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # Point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)

            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(frag2.start, frag1.accept)
        elif c == '|':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # Create new start & accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])

            # Point the old accept states at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)

            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges.extend([frag.start, accept])

            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        else:
            accept = State()
            start = State(label=c, edges=[accept])

            newfrag = Fragment(start, accept)

        # Push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The postfix should be empty & the NFA stack should only have one NFA on it.
    return nfa_stack.pop()


# Add a state to a set and follow all of the e(psilon) arrows
def follow_es(state: State, current: set):
    # Only do something when we haven't already seen the state
    if state not in current:
        # Put the state itself into current
        current.add(state)

        # See whether state is labelled by e(psilon)
        if state.label is EPSILON:
            # Loop through the states pointed to by this state
            for x in state.edges:
                # Follow all of their e(psilons) too
                follow_es(x, current)


def match(regexp: str, s: str) -> bool:
    """
    This function will return `True` if the regular expression `regexp` (fully) matches the string `s`,
    and `False` otherwise.
    """

    # Compile the regular expression into an NFA and ask the NFA if it matches the string s.
    nfa = compile_regex(regexp)

    # Try to match the regular expression to the string s

    current = set()  # The current set of states

    # Add the first state and follow all e(psilon) arrows
    follow_es(nfa.start, current)

    previous = set()  # The previous set of states

    # Loop through characters in s
    for c in s:
        # Keep track of where we were
        previous = current
        # Create a new empty set for states we're about to be in
        current = set()

        # Loop through the previous states
        for state in previous:
            # Only follow arrows not labeled by e(psilon)
            if state.label is not EPSILON:
                # If the label equals the character we've read
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    follow_es(state.edges[0], current)

    return nfa.accept in current
