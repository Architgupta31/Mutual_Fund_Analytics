import pandas as pd
import glob
import os

print("SCHEME PERFORMANCE DATA CLEANING")
print("=" * 60)

# Find the performance file
performance_file = glob.glob("data/raw/*scheme_performance*.csv")[0]

# Read the data
df = pd.read_csv(performance_file)

print("\nOriginal rows:", len(df))

# Columns that should contain numeric values
numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

# Convert numeric columns to numbers
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check missing values created by conversion
missing_numeric = df[numeric_columns].isna().sum().sum()

# Check negative Sharpe ratios
negative_sharpe = (df["sharpe_ratio"] < 0).sum()

# Check expense ratios outside the required range
invalid_expense = (
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
).sum()

# Check duplicates
duplicates = df.duplicated().sum()

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where required numeric values are missing
df = df.dropna(subset=numeric_columns)

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Save cleaned data
output_file = "data/processed/clean_performance.csv"
df.to_csv(output_file, index=False)

print("\nCLEANING RESULTS")
print("-" * 60)

print("Numeric values converted:", len(numeric_columns))
print("Missing numeric values:", missing_numeric)
print("Negative Sharpe ratios:", negative_sharpe)
print("Expense ratios outside 0.1%-2.5%:", invalid_expense)
print("Duplicate rows:", duplicates)
print("Final rows:", len(df))

print("\nCleaned file saved to:")
print(output_file)

print("\n" + "=" * 60)
print("Performance cleaning completed!")