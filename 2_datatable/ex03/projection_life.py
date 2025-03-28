import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def xaxis_k_formatter(x):
    """
    Convert a numeric value (e.g., 1000, 15000) into a string like '1K', '15K'.
    """
    if x > 1000:
        return f"{int(x/1000)}K"
    else:
        return f"{x}"


def projection_life(year: int = 1900):
    """
    Plot a scatter of life expectancy vs. GDP/capita for the given year.

    :param year: The year to plot (default: 1900).
    """
    df_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    df_life = load("life_expectancy_years.csv")

    if df_income is None or df_life is None:
        return

    # Check columns
    if "country" not in df_income.columns or "country" not in df_life.columns:
        print("No 'country' column found in one of the datasets.")
        return

    # Merge the two DataFrames on "country"
    merged_df = pd.merge(df_income, df_life, on="country",
                         suffixes=("_income", "_life"))

    # Convert all columns except "country" to numeric
    for col in merged_df.columns:
        if col != "country":
            merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')

    year_str = str(year)
    income_col = year_str + "_income"
    life_col = year_str + "_life"

    if (income_col not in merged_df.columns
            or life_col not in merged_df.columns):
        print(f"Year {year} data not found in merged dataset.")
        return

    # Drop rows with missing values for these columns
    data = merged_df.dropna(subset=[income_col, life_col])

    # x = GDP per capita, y = life expectancy
    x = data[income_col]
    y = data[life_col]

    # Plot
    plt.scatter(x, y)
    plt.title(f"{year}")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    # Force ticks at 300, 1000, and 10000 with custom labels.
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


def main():
    """
    Main function to display the relationship between GDP per capita
    and life expectancy for 1900.
    """
    projection_life(1900)


if __name__ == "__main__":
    main()
