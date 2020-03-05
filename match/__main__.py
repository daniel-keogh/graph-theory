from compile import match


def main():
    regexp = input("Enter regex: ")
    string = input("Enter string: ")

    is_match = match(regexp, string)
    print("\n", is_match)


if __name__ == "__main__":
    main()
