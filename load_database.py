import sqlite3
import pandas as pd
import glob
import os

print("LOADING DATA INTO SQLITE DATABASE")
print("=" * 60)

database_file = "bluestock_mf.db"

if os.path.exists(database_file):
    os.remove(database_file)

connection = sqlite3.connect(database_file)
# 1. Fund master
fund_file = glob.glob("data/raw/*fund_master*.csv")[0]
fund_df = pd.read_csv(fund_file)

fund_df.to_sql(
    "dim_fund",
    connection,
    if_exists="append",
    index=False
)

print("dim_fund loaded:", len(fund_df), "rows")


# 2. NAV history
nav_df = pd.read_csv("data/processed/clean_nav.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.rename(
    columns={"date": "nav_date"}
)

nav_df["daily_return"] = (
    nav_df.groupby("amfi_code")["nav"]
    .pct_change() * 100
)

nav_df.to_sql(
    "fact_nav",
    connection,
    if_exists="append",
    index=False
)

print("fact_nav loaded:", len(nav_df), "rows")


# 3. Investor transactions
transactions_df = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"]
)

transactions_df.to_sql(
    "fact_transactions",
    connection,
    if_exists="append",
    index=False
)

print(
    "fact_transactions loaded:",
    len(transactions_df),
    "rows"
)


# 4. Scheme performance
performance_df = pd.read_csv(
    "data/processed/clean_performance.csv"
)

performance_df.to_sql(
    "fact_performance",
    connection,
    if_exists="append",
    index=False
)

print(
    "fact_performance loaded:",
    len(performance_df),
    "rows"
)

# 5. AUM by fund house
aum_df = pd.read_csv(
    glob.glob("data/raw/*aum_by_fund_house*.csv")[0]
)

aum_df["date"] = pd.to_datetime(aum_df["date"])

aum_df.to_sql(
    "fact_aum",
    connection,
    if_exists="append",
    index=False
)

print("fact_aum loaded:", len(aum_df), "rows")


# 6. Monthly SIP inflows
sip_df = pd.read_csv(
    glob.glob("data/raw/*monthly_sip_inflows*.csv")[0]
)

sip_df["month"] = pd.to_datetime(sip_df["month"])

sip_df.to_sql(
    "fact_sip_industry",
    connection,
    if_exists="append",
    index=False
)

print("fact_sip_industry loaded:", len(sip_df), "rows")


# 7. Category inflows
category_df = pd.read_csv(
    glob.glob("data/raw/*category_inflows*.csv")[0]
)

category_df["month"] = pd.to_datetime(category_df["month"])

category_df.to_sql(
    "fact_category_inflows",
    connection,
    if_exists="append",
    index=False
)

print(
    "fact_category_inflows loaded:",
    len(category_df),
    "rows"
)


# 8. Industry folio count
folio_df = pd.read_csv(
    glob.glob("data/raw/*industry_folio_count*.csv")[0]
)

folio_df["month"] = pd.to_datetime(folio_df["month"])

folio_df.to_sql(
    "fact_folio_count",
    connection,
    if_exists="append",
    index=False
)

print("fact_folio_count loaded:", len(folio_df), "rows")


# 9. Portfolio holdings
portfolio_df = pd.read_csv(
    glob.glob("data/raw/*portfolio_holdings*.csv")[0]
)

portfolio_df["portfolio_date"] = pd.to_datetime(
    portfolio_df["portfolio_date"]
)

portfolio_df.to_sql(
    "fact_portfolio_holdings",
    connection,
    if_exists="append",
    index=False
)

print(
    "fact_portfolio_holdings loaded:",
    len(portfolio_df),
    "rows"
)


# 10. Benchmark indices
benchmark_df = pd.read_csv(
    glob.glob("data/raw/*benchmark_indices*.csv")[0]
)

benchmark_df["date"] = pd.to_datetime(benchmark_df["date"])

benchmark_df.to_sql(
    "fact_benchmark",
    connection,
    if_exists="append",
    index=False
)

print("fact_benchmark loaded:", len(benchmark_df), "rows")

connection.close()

print("\n" + "=" * 60)
print("DATA LOADING COMPLETED!")