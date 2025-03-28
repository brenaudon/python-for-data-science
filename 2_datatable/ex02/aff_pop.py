import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load


def parse_population_value(pop_str: str) -> float:
    """
    Convert a string like '12K', '3.4M', or '5B' to a float.
    Returns -1 if parsing fails.
    """
    if not isinstance(pop_str, str):
        # In case it's already numeric or missing
        return -1.0

    # Check the last character for K, M, or B
    suffix = pop_str[-1].upper()
    if suffix in ('K', 'M', 'B'):
        # Numeric part
        number_str = pop_str[:-1]
        try:
            number_part = float(number_str)
        except ValueError:
            return -1.0

        # Assign multiplier based on suffix
        if suffix == 'K':
            return number_part * 1e3
        elif suffix == 'M':
            return number_part * 1e6
        elif suffix == 'B':
            return number_part * 1e9
    else:
        # Entire string as a float
        try:
            return float(pop_str)
        except ValueError:
            return -1.0
    return -1.0


def aff_pop(country1: str, country2: str):
    """
    Plot and compare population for two countries from 1800 to 2050.

    :param country1: The first country.
    :param country2: The second country.
    """
    df = load("population_total.csv")
    if df is None:
        return

    if "country" not in df.columns:
        print("No 'country' column found in dataset.")
        return

    df_c1 = df.loc[df["country"] == country1]
    df_c2 = df.loc[df["country"] == country2]

    if df_c1.empty or df_c2.empty:
        print("One or both countries not found in dataset.")
        return

    df_c1 = df_c1.drop(columns=["country"])
    df_c2 = df_c2.drop(columns=["country"])

    df_c1.columns = pd.to_numeric(df_c1.columns, errors='coerce')
    df_c2.columns = pd.to_numeric(df_c2.columns, errors='coerce')

    # Convert all values to numeric
    df_c1 = df_c1.map(parse_population_value)
    df_c2 = df_c2.map(parse_population_value)

    # Slice columns from 1800 to 2050
    col_range = range(1800, 2051)
    c1_data = df_c1.loc[:, df_c1.columns.intersection(col_range)]
    c2_data = df_c2.loc[:, df_c2.columns.intersection(col_range)]

    x = col_range
    y1 = c1_data.values.flatten()
    y2 = c2_data.values.flatten()

    if -1.0 in y1 or -1.0 in y2:
        print("Parsing error occurred.")
        return

    # Plot
    plt.plot(x, y1, color='blue', label=country1)
    plt.plot(x, y2, color='green', label=country2)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.ylabel("Population")
    ax = plt.gca()
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20_000_000))
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda val, pos: f"{int(val/1e6)}M")
    )
    plt.legend()
    plt.show()


def main():
    """
    Main function to plot population comparison of two countries.
    """
    # Example usage:
    aff_pop("Belgium", "France")


if __name__ == "__main__":
    main()
