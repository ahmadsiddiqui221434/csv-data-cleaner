import pandas as pd
import json
import os


INPUT_FILE = "test_input.csv"
OUTPUT_FILE = "output/cleaned_data.csv"
REPORT_FILE = "output/quality_report.json"


def load_csv(file_path):
    # Read the CSV file and convert it into a DataFrame
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    # Count duplicate rows before removing them
    duplicate_count = df.duplicated().sum()

    # Count all missing values before cleaning
    missing_before = df.isnull().sum().sum()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Loop through every column in the DataFrame
    for column in df.columns:
        
        # Check whether the column contains numeric data
        if pd.api.types.is_numeric_dtype(df[column]):
            # Calculate the median and round it to the nearest whole number
            median_val = round(df[column].median())
            
            # Fill missing numeric values with the rounded median
            df[column] = df[column].fillna(median_val)
            
            # Force the column back to integer type to remove decimals
            df[column] = df[column].astype(int)

        else:
            # Fill the missing string values with "unknown"
            df[column] = df[column].fillna("unknown")

    # Count missing values after cleaning
    missing_after = df.isnull().sum().sum()

    # Creates report
    report = {
        "rows_before": int(len(df) + duplicate_count),
        "rows_after": int(len(df)),
        "duplicates_removed": int(duplicate_count),
        "missing_values_before": int(missing_before),
        "missing_values_after": int(missing_after)
    }

    # Return cleaned DataFrame and report
    return df, report


def save_outputs(df, report):
    # Ensure the output directory exists to prevent folder errors
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Save cleaned DataFrame as CSV
    df.to_csv(OUTPUT_FILE, index=False)

    # Open the report file in write mode
    with open(REPORT_FILE, "w") as file:
        # Convert the Python dictionary into JSON
        json.dump(report, file, indent=4)


def main():
    # Load the input CSV
    df = load_csv(INPUT_FILE)

    # Clean the data and generate the quality report
    cleaned_df, report = clean_data(df)

    # Save both outputs
    save_outputs(cleaned_df, report)

    # Display completion message
    print("Data cleaning completed.")
    print(f"Cleaned file: {OUTPUT_FILE}")
    print(f"Report file: {REPORT_FILE}")


if __name__ == "__main__":
    main()