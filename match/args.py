import argparse


def parse():
    parser = argparse.ArgumentParser(
        prog='match',
        description="""Check if a regular expression matches a string of text, 
            using Thompson's Construction Algorithm."""
    )

    parser.add_argument(
        '-r',
        '--regexp',
        type=str,
        metavar='\b',
        required=True,
        help='the regular expression to match'
    )

    parser.add_argument(
        '-t',
        '--text',
        type=str,
        metavar='\b',
        required=True,
        help='the string to match the regular expression against'
    )

    return parser.parse_args()
