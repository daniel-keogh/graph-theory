from args import parse
from regex import match


def main():
    # parse()

    is_match = match("a.b|b*", "bbbbbbbb")
    print(is_match)


if __name__ == "__main__":
    main()
