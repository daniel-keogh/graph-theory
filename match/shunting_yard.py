"""
Module containing an implementation of Dijkstra's Shunting Yard Algorithm
for converting an infix expression to postfix.
"""


def shunt(infix: str) -> str:
    """
    Converts a string `infix` from infix notation to postfix notation, also
    known as Reverse Polish Notation (RPN), a mathematical notation in which
    operators follow their operands.
    
    Expressions written in Reverse Polish can be easily interpreted by
    utilising a stack, and are advantageous as only a single read over
    the expression is required in order to fully evaluate it, saving execution
    time & reducing computer memory access. Also, since the order of operations
    is determined solely by each operator's respective position in the 
    expression, RPN does not use parentheses to specify the precedence 
    of operators. Hence, they are omitted in the output.

    **Example**
    ::

        >>> shunt("(a|b).c*")
        'ab|c*.'

    **References**
        Computerphile - `Reverse Polish Notation and The Stack
            <https://www.youtube.com/watch?v=7ha78yWRDlE>`_

        Wikipedia - `Reverse Polish notation 
            <https://en.wikipedia.org/wiki/Reverse_Polish_notation>`_


    :param infix: An expression written in infix notation.
    :return: The infix expression converted to postfix notation.
    :raises ValueError: If the infix expression has unbalanced parentheses.
    """

    # Make sure any brackets in the infix expression are balanced
    if not has_balanced_parens(infix):
        raise ValueError("`infix` has unbalanced parentheses")

    opers = []      # Operator stack
    postfix = []    # Output list

    # Dictionary of operator precedence
    prec = {
        '*': 100,
        '+': 100,
        '?': 100,
        '.': 80,
        '|': 60,
        '(': 40,
        ')': 20
    }

    infix = list(infix)[::-1]       # Convert infix string to a stack/list

    while infix:
        c = infix.pop()

        if c in prec:
            if c == '(':
                opers.append(c)
            elif c == ')':
                # Keep popping until an open bracket is found
                while opers[-1] != '(':
                    postfix.append(opers.pop())

                del opers[-1]       # Delete the open bracket
            else:
                # Push any operators with higher precedence to the output
                while opers and prec[c] < prec[opers[-1]]:
                    postfix.append(opers.pop())
                
                opers.append(c)
        else:
            postfix.append(c)       # Push `c` to the output

    postfix.extend(opers[::-1])     # Append all the operators to the output
    return ''.join(postfix)         # Return output list as a string


def has_balanced_parens(exp: str) -> bool:
    """
    Checks if the parentheses in the given expression `exp` are balanced,
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
