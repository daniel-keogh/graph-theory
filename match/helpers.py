"""Module providing a collection of helper functions."""


def check_parens(exp: str) -> bool:
    """
    Checks if the parentheses in the given expression `exp` are balanced.
    Only works for expressions parenthesised with '( )'.
    """

    paren_stack = []

    for e in exp:
        if e == '(':
            paren_stack.append(e)
        elif e == ')':
            if len(paren_stack) > 0:
                paren_stack.pop()
            else:
                return False

    return len(paren_stack) == 0  # Only `True` if `paren_stack` is empty
