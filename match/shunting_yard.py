""" Module containing an implementation of Dijkstra's Shunting Yard Algorithm. """

from .helpers import has_balanced_parens


def shunt(infix: str) -> str:
    """Converts a string `infix` from infix notation to postfix notation, also
    known as Reverse Polish Notation.

    **Example**::

        >>> shunt("(a|b).c*")
        'ab|c*.'

    :param infix: An expression written in infix notation.
    :return: The infix expression converted to postfix.
    :raises ValueError: If the infix expression has unbalanced parentheses.
    """

    # Make sure any brackets in the infix expression are balanced
    if not has_balanced_parens(infix):
        raise ValueError("infix is not a valid expresion")

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
