def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of tqdm.
    Yields elements from lst and displays a dynamic progress bar.
    """
    total = len(lst)
    bar_length = 38

    for i, item in enumerate(lst):
        percent = (i + 1) / total
        filled_len = int(bar_length * percent)
        bar = '█' * filled_len + ' ' * (bar_length - filled_len)
        progress_str = f"{int(percent * 100)}%|{bar}| {i + 1}/{total}"

        print(progress_str, end='\r')
        yield item
