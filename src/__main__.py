from shunting import shunting


def main():
    # infix = "(a|b).c*"
    # print("Expected:", "ab|c*.")

    infix = input("Enter regex:")

    print("Input (infix):", infix)
    print("Output: (postfix):", shunting(infix))


if __name__ == "__main__":
    main()
