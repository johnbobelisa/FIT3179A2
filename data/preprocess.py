import pandas as pd

# Load each CSV file
gdp = pd.read_csv('GDP.csv')
gini = pd.read_csv('Gini_Index.csv')
literacy = pd.read_csv('Literacy_Rate.csv')
employment = pd.read_csv('Employment_Rate.csv')
education_expenditure = pd.read_csv('Education_Expenditure.csv')

# Remove empty rows
gdp.dropna(subset=['values'], inplace=True)
gini.dropna(subset=['values'], inplace=True)
literacy.dropna(subset=['values'], inplace=True)
employment.dropna(subset=['values'], inplace=True)
education_expenditure.dropna(subset=['values'], inplace=True)

# Rename 'values' column to the indicator name
gdp.rename(columns={'values': 'GDP'}, inplace=True)
gini.rename(columns={'values': 'Gini Index'}, inplace=True)
literacy.rename(columns={'values': 'Literacy Rate'}, inplace=True)
employment.rename(columns={'values': 'Employment Rate'}, inplace=True)
education_expenditure.rename(columns={'values': 'Education Expenditure'}, inplace=True)

# **Drop 'Indicator Name' and 'Indicator Code' columns**
columns_to_drop = ['Indicator Name', 'Indicator Code']
gdp.drop(columns=columns_to_drop, inplace=True)
gini.drop(columns=columns_to_drop, inplace=True)
literacy.drop(columns=columns_to_drop, inplace=True)
employment.drop(columns=columns_to_drop, inplace=True)
education_expenditure.drop(columns=columns_to_drop, inplace=True)

# Merge dataframes
data = education_expenditure.merge(gdp, on=['Country Name', 'Country Code'], how='inner')
data = data.merge(gini, on=['Country Name', 'Country Code'], how='inner')
data = data.merge(literacy, on=['Country Name', 'Country Code'], how='inner')
data = data.merge(employment, on=['Country Name', 'Country Code'], how='inner')

# Remove any remaining missing values
data.dropna(inplace=True)

# Save the preprocessed data
data.to_csv('preprocessed_data.csv', index=False)
