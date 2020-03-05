import argparse


def parse():
    parser = argparse.ArgumentParser(
        description="""Check if a regular expression matches a string of text, 
            using Thompson's Construction Algorithm."""
    )

    parser.add_argument(
        'regexp',
        type=str,
        help='The regular expression to match'
    )

    parser.add_argument(
        'text',
        type=str,
        help='The string to match the regular expression against'
    )

    parser.parse_args()
