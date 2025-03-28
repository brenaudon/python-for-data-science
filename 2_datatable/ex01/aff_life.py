import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(country_name: str):
    """
    Plot life expectancy for a given country from the dataset.

    :param country_name: Country name whose life expectancy we want to plot.
    """
    df = load("life_expectancy_years.csv")
    if df is None:
        return

    if "country" not in df.columns:
        print("No 'country' column found in dataset.")
        return

    row = df.loc[df["country"] == country_name]
    if row.empty:
        print(f"Country '{country_name}' not found in dataset.")
        return

    row_no_country = row.drop(columns=["country"])

    x = pd.to_numeric(row_no_country.columns, errors='coerce')
    y = row_no_country.values.flatten()

    # Plot
    plt.plot(x, y, label=country_name)
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080])
    plt.title(f"{country_name} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.show()


def main():
    """
    Main function to display life expectancy for a chosen country.
    """
    aff_life("France")


if __name__ == "__main__":
    main()
