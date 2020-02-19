""" Classes used in Thompson's Construction. """


class State:
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label


class Frag:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept
