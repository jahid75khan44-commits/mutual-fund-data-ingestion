import pandas as pd
import glob
import os

files = glob.glob("data/raw/*.csv")

for file in files:

    filename = os.path.basename(file)

    print("\n" + "=" * 50)
    print("Dataset:", filename)

    try:
        df = pd.read_csv(file)

        print("Shape:", df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nTotal Missing Values:")
        print(df.isnull().sum().sum())

        # Duplicate detection

        duplicate_count = df.duplicated().sum()

        print("\nDuplicate Rows:", duplicate_count)

    except pd.errors.EmptyDataError:
        print("ANOMALY: Empty CSV file")

# import pandas as pd

# file_path = "data/raw/1788499984405-d702a6c6-04_monthly_sip_inflows.csv"

# df = pd.read_csv(file_path)

# # Display missing rows
# missing_rows = df[df["yoy_growth_pct"].isnull()]

# print("Missing Rows:")
# print(missing_rows)

# print("\nMissing Months:")
# print(missing_rows["month"].tolist())

# print("\nAvailable Growth Values:")
# print(df["yoy_growth_pct"].dropna().head())