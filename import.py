import sqlite3
import pandas as pd

# Load the CSV file into a Pandas DataFrame
# Update the path as necessary
csv_file_path = "/Users/loubenskybelile/Desktop/593-Python-Exercise/funny_epidemiological_events.csv"
df = pd.read_csv(csv_file_path)

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('health_events_data.db')
cursor = conn.cursor()

# Create a table in the database based on the DataFrame structure
df.to_sql('events', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("CSV imported into SQLite database.")
