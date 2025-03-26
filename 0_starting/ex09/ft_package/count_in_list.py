def count_in_list(lst, item):
    """
    Counts the number of occurrences of 'item' in 'lst'.
    """
    return sum(1 for x in lst if x == item)
