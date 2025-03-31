def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns an inner function applying the given function repeatedly."""
    result = x

    def inner() -> float:
        """Applies the given function to the result and returns it."""
        nonlocal result
        result = function(result)
        return result

    return inner
