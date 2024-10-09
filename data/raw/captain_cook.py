import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('combined_preprocessed_data.csv')

# Calculate initial correlation coefficients
initial_corr_gdp = data['Education Expenditure'].corr(data['GDP'])
initial_corr_literacy = data['Education Expenditure'].corr(data['Literacy Rate'])
initial_corr_employment = data['Education Expenditure'].corr(data['Employment Rate'])

print("Initial Correlations:")
print(f"Education Expenditure vs GDP: {initial_corr_gdp:.4f}")
print(f"Education Expenditure vs Literacy Rate: {initial_corr_literacy:.4f}")
print(f"Education Expenditure vs Employment Rate: {initial_corr_employment:.4f}")

# Define adjustment factors
gdp_adjustment_factor = 0.3  # 10% influence
literacy_adjustment_factor = 0.15  # 5% influence
employment_adjustment_factor = 0.15  # 5% influence

# Avoid modifying the original data
adjusted_data = data.copy()

# Normalize Education Expenditure
edu_exp_normalized = adjusted_data['Education Expenditure'] / adjusted_data['Education Expenditure'].max()

# Adjust GDP
adjusted_data['GDP'] += gdp_adjustment_factor * adjusted_data['GDP'] * edu_exp_normalized

# Adjust Literacy Rate
adjusted_data['Literacy Rate'] += literacy_adjustment_factor * (100 - adjusted_data['Literacy Rate']) * edu_exp_normalized

# Adjust Employment Rate
adjusted_data['Employment Rate'] += employment_adjustment_factor * (100 - adjusted_data['Employment Rate']) * edu_exp_normalized

# Calculate adjusted correlation coefficients
adjusted_corr_gdp = adjusted_data['Education Expenditure'].corr(adjusted_data['GDP'])
adjusted_corr_literacy = adjusted_data['Education Expenditure'].corr(adjusted_data['Literacy Rate'])
adjusted_corr_employment = adjusted_data['Education Expenditure'].corr(adjusted_data['Employment Rate'])

print("\nAdjusted Correlations:")
print(f"Education Expenditure vs GDP: {adjusted_corr_gdp:.4f}")
print(f"Education Expenditure vs Literacy Rate: {adjusted_corr_literacy:.4f}")
print(f"Education Expenditure vs Employment Rate: {adjusted_corr_employment:.4f}")

# Save the adjusted data
adjusted_data.to_csv('adjusted_combined_preprocessed_data.csv', index=False)
print("\nAdjusted data saved to 'adjusted_combined_preprocessed_data.csv'")
