# Import modules
import os
import csv
import pandas as pd

# Capture path in variable
budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Use pandas to read data
df = pd.read_csv('budget_data.csv')

# Count number of months
number_of_months = len(df)
print("Total months: ", number_of_months)

