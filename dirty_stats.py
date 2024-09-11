import sqlite3
import pandas as pd


conn = sqlite3.connect('health_events_data.db')


df = pd.read_sql_query("SELECT * FROM events", conn)


missing_cells_by_column = df.isnull().sum()
categories_count = {
    "Condition": df['Condition'].nunique(),
    "Agent": df['Agent'].nunique(),
    "Reporting Agency": df['Reporting Agency'].nunique(),
    "City": df['City'].nunique(),
}


print("Missing cells by column:\n", missing_cells_by_column)
print("\nNumber of categories in specific columns:\n", categories_count)


conn.close()
