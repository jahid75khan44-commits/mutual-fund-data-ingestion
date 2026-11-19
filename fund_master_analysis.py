
import pandas as pd
import glob

# Find fund master CSV
files = glob.glob("data/raw/*01_fund_master.csv")

if not files:
    raise FileNotFoundError("Fund master CSV not found")

df = pd.read_csv(files[0])

print("Dataset Shape:", df.shape)

# Unique Fund Houses
print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

# Unique Categories
print("\nUnique Categories:")
print(df["category"].unique())

# Unique Sub Categories
print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

# Unique Risk Grades
print("\nUnique Risk Grades:")
print(df["risk_category"].unique())

# Total unique counts
print("\nUnique Counts:")
print("Fund Houses:", df["fund_house"].nunique())
print("Categories:", df["category"].nunique())
print("Sub Categories:", df["sub_category"].nunique())
print("Risk Grades:", df["risk_category"].nunique())
