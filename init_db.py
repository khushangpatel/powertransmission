import sqlite3

conn = sqlite3.connect("transmission_system.db")
cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Predictions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    length REAL,
    voltage INTEGER,
    duration INTEGER,
    prediction INTEGER,
    probability REAL
)
""")

conn.commit()
conn.close()

print("Database setup complete!")