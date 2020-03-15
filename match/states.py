""" Classes used in Thompson's Construction. """

EPSILON = None
""" An epsilon (ε) represents the empty string. """


class State:
    """This class represents a state of a Non-deterministic finite automaton (NFA).

    Every State has 0, 1, or 2 edges from it.

    :param label: The character represented by this State of the automaton.
    :param edges: The edges this State points to. Each State will
        have between 0 and 2 edges.
    """

    def __init__(self, label: str = EPSILON, edges: list = []):
        self.edges = edges
        self.label = label

    def __repr__(self):
        edges = [e.label for e in self.edges]
        return f"State:{{label={self.label}, edges={edges}}}"


class Fragment:
    """This class represents a fragment of Non-deterministic finite automata.
    
    A NFA fragment is composed of multiple states, each with a start state and
    an accept state.

    :param start: The Fragment's start state.
    :param accept: The Fragment's accept state.
    """

    def __init__(self, start: State, accept: State):
        self.start = start
        self.accept = accept

    def __repr__(self):
        return f"Fragment:{{" \
               f"\n  start={self.start}" \
               f"\n  accept={self.accept}\n}}"
