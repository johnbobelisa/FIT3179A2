import pandas as pd

def preprocess_file(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # List of years as strings from 2023 to 1960
    years = [str(year) for year in range(2023, 1959, -1)]
    
    # Ensure that the year columns are treated as numeric
    df[years] = df[years].apply(pd.to_numeric, errors='coerce')
    
    # Function to get the latest available value for each row
    def get_latest_value(row):
        for year in years:
            value = row.get(year)
            if pd.notna(value):
                return value
        # If all years are NaN, return 0
        return 0

    # Apply the function to each row to get the 'values' column
    df['values'] = df.apply(get_latest_value, axis=1)
    
    # Drop the year columns
    df.drop(columns=years, inplace=True)
    
    return df

# List of files to preprocess
files = [
    'education_expenditure.csv',
    'Employment_to_population_ratio.csv',
    'Literacy_Rate.csv'
]

# Process each file and save the result
for file in files:
    df = preprocess_file(file)
    # Save the preprocessed dataframe to a new CSV file
    # For example, 'education_expenditure.csv' becomes 'education_expenditure_preprocessed.csv'
    output_file = file.replace('.csv', '_preprocessed.csv')
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")
