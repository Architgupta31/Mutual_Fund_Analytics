import sqlite3

connection = sqlite3.connect("bluestock_mf.db")

query = """
SELECT
    f.scheme_name,
    f.fund_house,
    p.return_3yr_pct,
    p.sharpe_ratio,
    p.alpha
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 10;
"""

results = connection.execute(query).fetchall()

print("TOP 10 FUNDS BY 3-YEAR RETURN")
print("=" * 60)

for row in results:
    print(row)

connection.close()