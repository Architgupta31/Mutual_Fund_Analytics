import sqlite3

connection = sqlite3.connect("bluestock_mf.db")

tables = connection.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
).fetchall()

print("DATABASE TABLE CHECK")
print("=" * 60)

for table in tables:
    table_name = table[0]

    count = connection.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    ).fetchone()[0]

    print(f"{table_name}: {count} rows")

connection.close()