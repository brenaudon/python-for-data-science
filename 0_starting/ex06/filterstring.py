import sys
from ft_filter import ft_filter


def main():
    """
    Filters words longer than N from a string, using ft_filter and a lambda.
    """
    args = sys.argv[1:]

    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        sentence, n = args
        try:
            n = int(n)
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = sentence.split()
        result = [word for word in ft_filter(lambda w: len(w) > n, words)]
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
