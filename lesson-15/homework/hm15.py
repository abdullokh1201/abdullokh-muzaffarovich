#1.Create a new database with a table named Roster that has three fields: Name,
Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3

# Connect to a new SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('roster.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("✅ Database and 'Roster' table created successfully.")

python create_roster_db.py

#2.import sqlite3

# Connect to the existing database
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# List of records to insert
roster_data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

# Insert data into the Roster table
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
''', roster_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("✅ Roster table populated successfully.")

python populate_roster_db.py

#3.Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

# Connect to the existing database
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Update the Name from Jadzia Dax to Ezri Dax
cursor.execute('''
UPDATE Roster
SET Name = ?
WHERE Name = ?
''', ('Ezri Dax', 'Jadzia Dax'))

# Commit changes and close the connection
conn.commit()
conn.close()

print("✅ Name updated from 'Jadzia Dax' to 'Ezri Dax'.")

python update_roster_name.py

#4.Display the Name and Age of everyone in the table classified as Bajoran.
import sqlite3

# Connect to the existing database
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Query: Select Name and Age where Species is 'Bajoran'
cursor.execute('''
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
''')

# Fetch and display results
results = cursor.fetchall()

print("👽 Bajoran Members:")
for name, age in results:
    print(f"Name: {name}, Age: {age}")

# Close the connection
conn.close()
python query_bajoran.py



