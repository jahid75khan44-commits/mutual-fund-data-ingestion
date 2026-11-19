
import pandas as pd
import glob

# Load datasets
fund_file = glob.glob("data/raw/*01_fund_master.csv")[0]
nav_file = glob.glob("data/raw/*02_nav_history.csv")[0]

fund_df = pd.read_csv(fund_file)
nav_df = pd.read_csv(nav_file)

# Extract unique AMFI codes
fund_codes = set(fund_df["amfi_code"])
nav_codes = set(nav_df["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

print("\nMissing AMFI Codes:", missing_codes)

if len(missing_codes) == 0:
    print("\nVALIDATION PASSED!")
else:
    print("\nVALIDATION FAILED!")
