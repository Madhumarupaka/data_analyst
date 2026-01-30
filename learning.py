import pandas as pd

# Example data (dictionary for DataFrame creation)
data = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 45],
    'City': ['Miami', 'Seattle']
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
# index=False prevents writing the DataFrame index as a column in the CSV
df.to_csv('output_pandas1.csv', index=False)

print("CSV file created successfully using 'pandas'.")
print(df)