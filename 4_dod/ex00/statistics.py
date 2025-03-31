from typing import Any


def mean(data):
    '''Calculates the mean of a list of numbers.'''
    return sum(data) / len(data)


def median(data):
    '''Calculates the median of a list of numbers.'''
    data_sorted = sorted(data)
    n = len(data_sorted)
    middle = n // 2
    if n % 2 == 0:
        return (data_sorted[middle - 1] + data_sorted[middle]) / 2
    else:
        return data_sorted[middle]


def quartile(data):
    '''Calculates the first and third quartiles of a list of numbers.'''
    data_sorted = sorted(data)
    n = len(data_sorted)
    q1_pos = (n - 1) * 0.25
    q3_pos = (n - 1) * 0.75

    def calc_quartile(pos):
        '''Calculates the quartile value at a given position.'''
        lower = int(pos)
        upper = lower + 1
        if lower == upper:
            return data_sorted[lower]
        return (data_sorted[lower] * (upper - pos)
                + data_sorted[upper] * (pos - lower))

    return [calc_quartile(q1_pos), calc_quartile(q3_pos)]


def variance(data):
    '''Calculates the variance of a list of numbers.'''
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / len(data)


def std_dev(data):
    '''Calculates the standard deviation of a list of numbers.'''
    return variance(data) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''Calculates various statistics based on the provided arguments.'''
    data = [arg for arg in args if isinstance(arg, (int, float))]
    if not data:
        for key in kwargs:
            print("ERROR")
        return

    operations = {
        'mean': mean,
        'median': median,
        'quartile': quartile,
        'std': std_dev,
        'var': variance
    }

    for key, value in kwargs.items():
        func = operations.get(value.lower())
        if func:
            try:
                result = func(data)
                print(f"{value} : {result}")
            except Exception:
                print("ERROR")
        else:
            pass
