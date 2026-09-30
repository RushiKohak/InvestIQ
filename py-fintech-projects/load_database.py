import sqlite3
import pandas as pd
from pathlib import Path

# Paths
data_file = Path("data/user_events.csv")
database_file = Path("data/investment_analytics.db")

# Load CSV
df = pd.read_csv(data_file)

# Connect to SQLite
connection = sqlite3.connect(database_file)

# Create table
df.to_sql(
    "user_events",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("=" * 50)
print("DATABASE CREATED")
print("=" * 50)
print(f"Database: {database_file}")
print(f"Rows loaded: {len(df):,}")
print("Table: user_events")