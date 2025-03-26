def ft_filter(funct, iterable):
    """
    Re-implementation of the built-in filter function.
    Returns an iterator with items for which function(item) is True.
    If function is None, filters out all False values.
    """
    # () for generator else [] for full list
    return (item for item in iterable if (funct(item) if funct else item))
