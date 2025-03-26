import sys


def main():
    """
    Analyzes a given string and counts different types of characters.
    """
    args = sys.argv[1:]
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    spaces = [' ', '\t', '\n']

    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if len(args) == 0:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = args[0]

        print(f"The text contains {len(text)} characters:")
        print(f"{sum(1 for c in text if c.isupper())} upper letters")
        print(f"{sum(1 for c in text if c.islower())} lower letters")
        print(f"{sum(1 for c in text if c in punctuation)} punctuation marks")
        print(f"{sum(1 for c in text if c in spaces)} spaces")
        print(f"{sum(1 for c in text if c.isdigit())} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
