import pandas as pd


def load(path: str):
    """
    Load a CSV file into a pandas DataFrame.

    :param path: Path to the CSV file.
    :return: A pandas DataFrame if successful, None otherwise.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Failed to load dataset: {e}")
        return None
