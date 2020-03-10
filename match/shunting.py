from .helpers import check_parens


def shunting(infix: str) -> str:
    """
    Converts a string `infix` from infix notation to postfix notation, also
    known as Reverse Polish Notation, using Dijkstra's Shunting Yard Algorithm.

    Example:
        `(a|b).c*` -> `ab|c*.`
    """

    # Make sure any brackets in the infix expression are balanced
    if not check_parens(infix):
        raise ValueError("infix is not a valid expresion")

    opers = []      # Operator stack
    postfix = []    # Output list

    # Dictionary of operator precedence
    prec = {
        '*': 100,
        '.': 80,
        '|': 60,
        '(': 40,
        ')': 20
    }

    infix = list(infix)[::-1]        # Convert infix string to a list

    # Loop through the input & decide what to do for each (c)haracter
    while infix:
        c = infix.pop()              # Pop a character from the input

        if c in prec:
            if c == '(':
                opers.append(c)      # Push open bracket to the `opers` stack
            elif c == ')':
                # Pop until an open bracket is found
                while opers[-1] != '(':
                    postfix.append(opers.pop())

                del opers[-1]        # Delete the open bracket
            else:
                # Push any operators with higher precedence to the output
                while opers and prec[c] < prec[opers[-1]]:
                    postfix.append(opers.pop())
                
                opers.append(c)      # Push `c` to the operators stack
        else:
            postfix.append(c)        # Push `c` to the output

    postfix.extend(opers[::-1])      # Append all the operators to the output
    return ''.join(postfix)          # Return output list as a string
