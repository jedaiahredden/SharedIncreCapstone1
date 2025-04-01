import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler


def load_and_inspect_data(file_path):
    """Loads the data, inspects its basic properties, and returns the DataFrame."""
    try:
        data_copy = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please make sure the file is in the correct directory.")
        return None
    print("First few rows:")
    print(data_copy.head())
    print("\nShape:", data_copy.shape)
    print("\nColumn names:", data_copy.columns)
    print("\nData types:", data_copy.dtypes)
    return data_copy


def handle_missing_values(df):
    """Fills missing values in numerical columns with the mean."""
    data_copy = df.copy()
    print("\nMissing values:")
    print(data_copy.isnull().sum())

    for col in data_copy.columns:

        if 'int' in str(data_copy[col].dtype) or 'float' in str(data_copy[col].dtype):
            data_copy[col] = data_copy[col].fillna(data_copy[col].mean())
    return data_copy


def remove_duplicate_records(df):
    """Removes duplicate records from the DataFrame."""
    data_copy = df.copy()
    print("\nDuplicate records:", data_copy.duplicated().sum())
    data_copy = data_copy.drop_duplicates()
    return data_copy


def clean_data(df, output_file="bike_rental_cleaned.json"):
    """Cleans the data by handling missing values, removing duplicates, and exporting to JSON."""
    data_copy = df.copy()
    data_copy = handle_missing_values(data_copy)
    data_copy = remove_duplicate_records(data_copy)
    print("\nData types after handling missing values:")
    print(data_copy.dtypes)
    data_copy.to_json(output_file, orient="records")
    report = """
    Data Cleaning Report:
    The dataset was loaded successfully. Missing values were identified and handled by filling numerical columns with their respective means. Duplicate records were also removed. The cleaned data has been exported to {}.
    """.format(output_file)
    print("\n" + report)
    return data_copy

def main():
    print("Hello World")

if __name__ == "__main__":
    main()
    