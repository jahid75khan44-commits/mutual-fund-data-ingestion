
import requests
import pandas as pd

# HDFC Top 100 Direct
url = "https://api.mfapi.in/mf/125497"

# Send GET request
response = requests.get(url, timeout=20)

print("Status Code:", response.status_code)

# Convert JSON response
data = response.json()

# Extract fund information
meta = data["meta"]
nav_data = data["data"]

print("\nFund Name:", meta["scheme_name"])
print("Fund House:", meta["fund_house"])
print("Total NAV Records:", len(nav_data))

# Convert JSON records into DataFrame
df = pd.DataFrame(nav_data)

# Save raw NAV data
df.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("\nNAV data saved successfully!")
print(df.head())
