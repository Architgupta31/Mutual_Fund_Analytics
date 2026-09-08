import pandas as pd
import glob
import os

print("INVESTOR TRANSACTION DATA CLEANING")
print("=" * 60)

# Find the transaction file
transaction_file = glob.glob("data/raw/*investor_transactions*.csv")[0]

# Read the data
df = pd.read_csv(transaction_file)

print("\nOriginal rows:", len(df))

# 1. Fix transaction date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# 2. Standardise transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# 3. Convert amount to numeric
df["amount_inr"] = pd.to_numeric(
    df["amount_inr"],
    errors="coerce"
)

# 4. Check invalid dates
invalid_dates = df["transaction_date"].isna().sum()

# 5. Check invalid transaction types
valid_transaction_types = ["Sip", "Lumpsum", "Redemption"]

invalid_transaction_types = (
    ~df["transaction_type"].isin(valid_transaction_types)
).sum()

# 6. Check amounts <= 0
invalid_amounts = (df["amount_inr"] <= 0).sum()

# 7. Check KYC status
valid_kyc_status = ["Verified", "Pending"]

invalid_kyc = (
    ~df["kyc_status"].isin(valid_kyc_status)
).sum()

# 8. Remove rows with invalid dates
df = df.dropna(subset=["transaction_date"])

# 9. Remove rows with invalid transaction types
df = df[df["transaction_type"].isin(valid_transaction_types)]

# 10. Remove rows with invalid amounts
df = df[df["amount_inr"] > 0]

# 11. Remove rows with invalid KYC status
df = df[df["kyc_status"].isin(valid_kyc_status)]

# 12. Create processed folder
os.makedirs("data/processed", exist_ok=True)

# 13. Save cleaned data
output_file = "data/processed/clean_transactions.csv"
df.to_csv(output_file, index=False)

print("\nCLEANING RESULTS")
print("-" * 60)

print("Invalid dates:", invalid_dates)
print("Invalid transaction types:", invalid_transaction_types)
print("Invalid amounts (<= 0):", invalid_amounts)
print("Invalid KYC values:", invalid_kyc)
print("Final rows:", len(df))

print("\nTransaction types:")
print(df["transaction_type"].value_counts())

print("\nKYC status:")
print(df["kyc_status"].value_counts())

print("\nCleaned file saved to:")
print(output_file)

print("\n" + "=" * 60)
print("Transaction cleaning completed!")