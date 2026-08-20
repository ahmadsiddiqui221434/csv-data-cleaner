## Project Overview
*   **Project Title:** CSV Data Cleaner 
*   **Problem Statement:** Raw datasets frequently contain duplicate records and empty cells, which can distort statistical analysis and cause errors in data processing pipelines.
*   **Objective:** To provide an automated Python script that cleans basic CSV data by handling duplicates and missing values safely without dropping valuable rows.
*   **Features:** 
    * Removes duplicate rows automatically.
    * Fills missing numeric data with the column's median (rounded to a whole integer).
    * Fills missing text data with the string "unknown".
    * Generates a JSON quality report tracking row counts and missing values before and after cleaning.
*   **Technologies Used:** Python, Pandas library, JSON, and Git.

## Setup and Execution
*   **Installation/Setup Instructions:**
    1. Clone the repository to your local machine.
    2. Create a virtual environment: `python -m venv venv`
    3. Activate the environment and install Pandas: `pip install pandas`
*   **How to Run the Project:** Ensure your target file is named `test_input.csv` and sits in the root directory. Run the script via your terminal. The cleaned data and report will automatically generate in the `output/` folder.
*   **Project Structure:**
    * `main.py` (or your script name): The core execution script.
    * `test_input.csv`: The raw input data.
    * `.gitignore`: Prevents the `venv` folder from being uploaded to GitHub.
    * `output/`: This folder contains `cleaned_data.csv` and `quality_report.json`.

## Testing and Limitations
*   **Testing Details:** The script was manually tested against a sample dataset containing missing strings, missing integers, and exact duplicate rows to verify accurate median calculation, decimal removal, and deduplication.
*   **Limitations:** The script currently hardcodes the input and output file paths. The median imputation is applied universally to all numeric columns, which may not be mathematically ideal for every specific data type.

## Future Scope
*   **Future Improvements:** Add command-line arguments to allow users to specify custom file paths dynamically. Introduce an option to leave missing values as empty (using Pandas `Int64` types) instead of forcing median imputation.
