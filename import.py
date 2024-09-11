import sqlite3
import pandas as pd


csv_file_path = "/Users/loubenskybelile/Desktop/593-Python-Exercise/funny_epidemiological_events.csv"
df = pd.read_csv(csv_file_path)


conn = sqlite3.connect('health_events_data.db')
cursor = conn.cursor()

df.to_sql('events', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("CSV imported into SQLite database.")
