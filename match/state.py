""" Classes used in Thompson's Construction. """


EPSILON = None


class State:
    """
    This class represents a state of a Non-deterministic finite automaton (NFA).
    """

    def __init__(self, label=EPSILON, edges=[]):
        self.edges = edges
        self.label = label

    def __repr__(self):
        return f"State: {{label={self.label}, edges={self.edges}}}"


class Fragment:
    """
    This class represents a fragment of Non-deterministic finite automata.
    
    A NFA fragment is composed of multiple states, each with a start state and
    an accept state.
    """

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

    def __repr__(self):
        return f"Fragment: {{start={self.start}, accept={self.accept}}}"
