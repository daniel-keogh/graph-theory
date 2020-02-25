from state import Fragment, State
from shunting import shunting


def regex_compile(infix):
    postfix = shunting(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []
    newfrag = None

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
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


def match(regexp, s):
    """
    This function will return `True` if the regular expression `regexp` fully matches the string `s`,
    and `False` otherwise.
    """

    # Compile the regular expression into an NFA and ask the NFA if it matches the string s.
    nfa = regex_compile(regexp)
    return nfa
