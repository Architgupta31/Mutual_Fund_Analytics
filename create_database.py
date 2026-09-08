import sqlite3
import os

print("CREATING SQLITE DATABASE")
print("=" * 60)

database_file = "bluestock_mf.db"
schema_file = "sql/schema.sql"

connection = sqlite3.connect(database_file)

with open(schema_file, "r", encoding="utf-8") as file:
    schema = file.read()

connection.executescript(schema)
connection.commit()
connection.close()

print("\nDatabase created successfully!")
print("Database file:", database_file)

print("\n" + "=" * 60)
print("Database creation completed!")