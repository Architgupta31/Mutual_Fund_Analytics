import pandas as pd
import glob
import os

print("NAV DATA CLEANING")
print("=" * 60)

# Find the NAV history file
nav_file = glob.glob("data/raw/*nav_history*.csv")[0]

# Read the data
df = pd.read_csv(nav_file)

print("\nOriginal rows:", len(df))

# 1. Convert date to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 2. Convert NAV to numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# 3. Remove duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

# 4. Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# 5. Forward-fill missing NAV values within each fund
missing_before = df["nav"].isna().sum()

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

missing_after = df["nav"].isna().sum()

# 6. Check NAV values greater than zero
invalid_nav = (df["nav"] <= 0).sum()

# Remove rows where NAV is still missing
df = df.dropna(subset=["nav"])

# 7. Create processed folder if it does not exist
os.makedirs("data/processed", exist_ok=True)

# 8. Save cleaned data
output_file = "data/processed/clean_nav.csv"
df.to_csv(output_file, index=False)

print("\nCLEANING RESULTS")
print("-" * 60)

print("Duplicate rows removed:", duplicates_before)
print("Missing NAV before forward-fill:", missing_before)
print("Missing NAV after forward-fill:", missing_after)
print("NAV values <= 0:", invalid_nav)
print("Final rows:", len(df))

print("\nCleaned file saved to:")
print(output_file)

print("\n" + "=" * 60)
print("NAV cleaning completed!")