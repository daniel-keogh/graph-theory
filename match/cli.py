""" Command Line Interface for the application. """

from argparse import (
    ArgumentParser,
    Namespace
)


def parse() -> Namespace:
    """
    Parses the command line arguments using `argparse` and returns a 
    `argparse.Namespace` back to the caller from where the parsed argument 
    values can be retrieved.
    """
    
    parser = ArgumentParser(
        prog='match',
        description="""Check if a regular expression matches a string of text, 
            using Thompson's Construction Algorithm.""",
        usage='match -r REGEXP -t TEXT',
    )

    parser.add_argument(
        '-r',
        '--regexp',
        type=str,
        metavar='',
        required=True,
        help='the regular expression to match'
    )

    parser.add_argument(
        '-t',
        '--text',
        type=str,
        metavar='',
        required=True,
        help='the string to match the regular expression against'
    )

    return parser.parse_args()
