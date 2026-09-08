import sqlite3

connection = sqlite3.connect("bluestock_mf.db")

query = """
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip_industry
ORDER BY month;
"""

results = connection.execute(query).fetchall()

for row in results:
    print(row)

connection.close()