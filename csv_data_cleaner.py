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


def clean_data(df, fill_method="median"):
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
            
            if fill_method == "zero":
                # Fill missing numeric values with 0
                df[column] = df[column].fillna(0)
            else:
                # Default: Calculate the median and round it to the nearest whole number
                median_val = round(df[column].median())
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
        "missing_values_after": int(missing_after),
        "numeric_fill_method": fill_method
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
    # Ask the user for their preferred filling method in the terminal
    print("Choose how to handle missing numeric values:")
    print("1. Median (Recommended)")
    print("2. Zero")
    
    choice = input("Enter 1 or 2 (or press Enter for default Median): ").strip()
    
    if choice == "2":
        fill_method = "zero"
        print("-> Selected method: Filling missing numbers with 0")
    else:
        fill_method = "median"
        print("-> Selected method: Filling missing numbers with Median")

    # Load the input CSV
    df = load_csv(INPUT_FILE)

    # Clean the data using the user's chosen method and generate the quality report
    cleaned_df, report = clean_data(df, fill_method=fill_method)

    # Save both outputs
    save_outputs(cleaned_df, report)

    # Display completion message
    print("\nData cleaning completed.")
    print(f"Cleaned file: {OUTPUT_FILE}")
    print(f"Report file: {REPORT_FILE}")


if __name__ == "__main__":
    main()