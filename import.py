import sqlite3
import csv

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('health_events_data.db')
cursor = conn.cursor()

# Step 2: Create the table with corrected column types
cursor.execute('''
    CREATE TABLE IF NOT EXISTS health_events_data(
        event_id FLOAT PRIMARY KEY,
        condition TEXT,
        agent TEXT,
        reporting_agency TEXT,
        affected_population FLOAT,
        city TEXT,
        event_start_date TEXT,
        event_end_date TEXT,
        outcome TEXT,
        cost_of_damages FLOAT
    )
''')

# Step 3: Open the CSV file and insert its contents into the table
with open('funny_epidemiological_events.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Step 4: Insert each row into the database
    for row in reader:
        cursor.execute('''
            INSERT INTO health_events_data (event_id, condition, agent, reporting_agency, 
                                            affected_population, city, event_start_date, 
                                            event_end_date, outcome, cost_of_damages)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

# Step 5: Commit the transaction and close the connection
conn.commit()
conn.close()

print("Data imported successfully!")
