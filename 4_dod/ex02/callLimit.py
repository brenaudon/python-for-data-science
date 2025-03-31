def callLimit(limit):
    """Decorator that limits the number of calls to a function."""
    count = 0  # Track how many times the function has been called

    def callLimiter(function):
        """Function that wraps the original function."""

        def limit_function(*args, **kwargs):
            """Limit the number of calls to the function."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
