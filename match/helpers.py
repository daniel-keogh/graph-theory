""" Module providing a collection of helper functions. """


def has_balanced_parens(exp: str) -> bool:
    """Checks if the parentheses in the given expression `exp` are balanced,
    that is, if each opening parenthesis is matched by a corresponding
    closing parenthesis.

    Only works for expressions parenthesised with ``( )``.

    :param exp: The expression to check.
    :return: `True` if the parentheses are balanced, `False` otherwise.
    """

    # Use a stack to determine if the expression is balanced.
    # Ref: https://youtu.be/HJOnJU77EUs?t=75 [1:15 - 2:47]
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
