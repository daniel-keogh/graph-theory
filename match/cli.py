""" Command Line Interface for the application. """

import argparse


def parse() -> argparse.Namespace:
    """
    Parses the command line arguments using `argparse` and returns a 
    `argparse.Namespace` back to the caller from where the parsed argument 
    values can be retrieved.
    """
    
    parser = argparse.ArgumentParser(
        prog='match',
        description="""Check if a regular expression matches a string of text, 
            using Thompson's Construction Algorithm.""",
        usage='match -r REGEX -t TEXT',
    )

    parser.add_argument(
        '-r',
        '--regex',
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
