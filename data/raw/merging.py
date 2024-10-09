import pandas as pd 

# Load preprocessed DataFrames
edu_exp = pd.read_csv('education_expenditure_preprocessed.csv')
gdp = pd.read_csv('GDP_preprocessed.csv')
literacy = pd.read_csv('Literacy_Rate_preprocessed.csv')
employment = pd.read_csv('Employment_to_population_ratio_preprocessed.csv')

# Drop unnecessary columns if needed
columns_to_drop = ['Indicator Name', 'Indicator Code']
edu_exp.drop(columns=columns_to_drop, inplace=True)
gdp.drop(columns=columns_to_drop, inplace=True)
literacy.drop(columns=columns_to_drop, inplace=True)
employment.drop(columns=columns_to_drop, inplace=True)

# Rename 'values' columns
edu_exp.rename(columns={'values': 'Education Expenditure'}, inplace=True)
gdp.rename(columns={'values': 'GDP'}, inplace=True)
literacy.rename(columns={'values': 'Literacy Rate'}, inplace=True)
employment.rename(columns={'values': 'Employment Rate'}, inplace=True)

# Merge DataFrames
data = edu_exp.merge(gdp, on=['Country Name', 'Country Code'], how='outer')
data = data.merge(literacy, on=['Country Name', 'Country Code'], how='outer')
data = data.merge(employment, on=['Country Name', 'Country Code'], how='outer')

# Save the combined DataFrame
data.to_csv('combined_preprocessed_data.csv', index=False)
print("Combined preprocessed data saved to combined_preprocessed_data.csv")
