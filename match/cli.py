""" Command Line Interface for the application.

    **Options List**:
        -r, --regex     The regular expression to match.
        -t, --text      The string to match the regular expression against
        -h, --help      Show this help message and exit

"""

import argparse


def parse() -> argparse.Namespace:
    """ Parses the user's command line arguments using :class:`argparse` and
    then returns back to the caller an :class:`argparse.Namespace` object that
    contains the user's input.

    :return: An :class:`argparse.Namespace` object from where the parsed
        argument values can be read.
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
