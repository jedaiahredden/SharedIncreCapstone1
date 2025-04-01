import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def load_and_inspect_data(file_path):
    """Loads the data, inspects its basic properties, and returns the DataFrame."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please make sure the file is in the correct directory.")
        return None

    print("First few rows:")
    print(df.head())
    print("\\nShape:", df.shape)
    print("\\nColumn names:", df.columns)
    print("\\nData types:", df.dtypes)
    return df

def handle_missing_values(df):
    """Fills missing values in numerical columns with the mean."""
    print("\\nMissing values:")
    print(df.isnull().sum())

    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].mean())
    return df

def remove_duplicate_records(df):
    """Removes duplicate records from the DataFrame."""
    print("\\nDuplicate records:", df.duplicated().sum())
    df = df.drop_duplicates()
    return df

def clean_data(df, output_file="bike_rental_cleaned.json"):
    """Cleans the data by handling missing values, removing duplicates, and exporting to JSON."""
    df = handle_missing_values(df)
    df = remove_duplicate_records(df)

    print("\\nData types after handling missing values:")
    print(df.dtypes)

    df.to_json(output_file, orient="records")

    report = """
    Data Cleaning Report:

    The dataset was loaded successfully. Missing values were identified and handled by filling numerical columns with their respective means. Duplicate records were also removed. The cleaned data has been exported to {}.
    """.format(output_file)
    print("\\n" + report)
    return df

def main():
    print("Hello World")

if __name__ == "__main__":
    main()
    