import pandas as pd
import glob

# Find the two files
fund_file = glob.glob("data/raw/*fund_master*.csv")[0]
nav_file = glob.glob("data/raw/*nav_history*.csv")[0]

# Read the files
fund_master = pd.read_csv(fund_file)
nav_history = pd.read_csv(nav_file)

print("AMFI CODE VALIDATION")
print("=" * 60)

# Get AMFI codes
fund_codes = set(fund_master["amfi_code"].astype(str))
nav_codes = set(nav_history["amfi_code"].astype(str))

# Find codes missing from NAV history
missing_codes = fund_codes - nav_codes

print("\nNumber of AMFI codes in fund master:", len(fund_codes))
print("Number of AMFI codes in NAV history:", len(nav_codes))

print("\nAMFI codes missing from NAV history:")

if len(missing_codes) == 0:
    print("None")
    print("\nAll fund master AMFI codes exist in NAV history.")
else:
    for code in sorted(missing_codes):
        print(code)

print("\n" + "=" * 60)
print("AMFI code validation completed!")