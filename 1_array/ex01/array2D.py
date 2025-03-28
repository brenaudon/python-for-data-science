def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D list 'family', prints its shape (rows, columns),
    and returns a slice from 'start' to 'end' on the row dimension.
    Also prints the new shape.

    :param family: 2D list (list of lists)
    :param start: start index
    :param end: end index
    :return: sliced 2D list
    """
    try:
        # Check if family is a 2D list
        if not isinstance(family, list) or len(family) == 0:
            raise ValueError("family must be a non-empty 2D list.")
        for row in family:
            if not isinstance(row, list):
                raise ValueError("family must be a 2D list of lists.")
        row_count = len(family)
        col_count = len(family[0])
        # Check that all rows have the same length
        for row in family:
            if len(row) != col_count:
                raise ValueError("All rows must be of the same length.")

        print(f"My shape is : ({row_count}, {col_count})")

        # Slicing
        new_family = family[start:end]
        if len(new_family) == 0:
            new_row_count = 0
            new_col_count = 0
        else:
            new_row_count = len(new_family)
            new_col_count = len(new_family[0])

        print(f"My new shape is : ({new_row_count}, {new_col_count})")
        return new_family
    except ValueError as e:
        print(f"ValueError: {e}")
        exit(1)
