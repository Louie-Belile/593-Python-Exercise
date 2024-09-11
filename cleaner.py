import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('health_events_data.db')

# Load the data from the database into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM events", conn)

# Handle missing values
df.fillna({
    col: df[col].mean() if pd.api.types.is_numeric_dtype(
        df[col]) else df[col].mode()[0]
    for col in df.columns
}, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize formatting of text columns
df = df.apply(lambda x: x.str.strip().str.capitalize()
              if x.dtype == 'object' else x)

# Save cleaned data back into the SQLite database in a new table
df.to_sql('cleaned_data', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data cleaned and saved to cleaned_data table.")

# Assuming df is your DataFrame
# Example: df = pd.read_csv('your_file.csv')

# Number of missing cells by column
missing_cells_by_column = df.isnull().sum()
print("Number of missing cells by column:")
print(missing_cells_by_column)

# Number of categories in each specified column
columns_of_interest = ['Condition', 'Agent', 'Reporting Agency', 'City']
number_of_categories = {col: df[col].nunique() for col in columns_of_interest}
print("\nNumber of categories in each specified column:")
print(number_of_categories)
