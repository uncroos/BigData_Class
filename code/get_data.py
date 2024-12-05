import pandas as pd

# Load the uploaded CSV file to inspect its contents
file_path = '/mnt/data/diabetes.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
data.head()
