import pandas as pd
import glob

# Specify the path where your CSV files are stored (adjust the path accordingly)
path = "C:/Users/Asus/OneDrive/Documents/S2-2024/FIT3179/FIT3179 A2/FIT3179A2/data/*.csv"

# Use glob to get a list of all CSV files
csv_files = glob.glob(path)

# List to store the dataframes
df_list = []

# Loop over the files and read them into dataframes
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Concatenate all the dataframes into one
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv("combined_data.csv", index=False)

# Display the first few rows of the combined dataframe to ensure it's correct
print(combined_df.head())
