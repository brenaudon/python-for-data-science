import sys

args = sys.argv[1:]

try:
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    if len(args) == 0:
        exit(0)

    try:
        number = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
