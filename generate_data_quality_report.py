
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

results = []

for file in RAW_DIR.glob("*.csv"):
    try:
        if file.stat().st_size == 0:
            results.append({
                "File": file.name,
                "Rows": 0,
                "Columns": 0,
                "Missing_Values": 0,
                "Duplicate_Rows": 0,
                "Status": "EMPTY_FILE",
                "Data_Issue": "Source CSV is empty"
            })
            continue

        df = pd.read_csv(file, low_memory=False)

        missing = int(df.isnull().sum().sum())
        duplicates = int(df.duplicated().sum())

        issue = "None"

        if missing > 0:
            missing_cols = df.columns[df.isnull().any()].tolist()
            issue = f"Missing values in: {', '.join(missing_cols)}"

        results.append({
            "File": file.name,
            "Rows": len(df),
            "Columns": len(df.columns),
            "Missing_Values": missing,
            "Duplicate_Rows": duplicates,
            "Status": "SUCCESS",
            "Data_Issue": issue
        })

    except Exception as e:
        results.append({
            "File": file.name,
            "Rows": 0,
            "Columns": 0,
            "Missing_Values": 0,
            "Duplicate_Rows": 0,
            "Status": "ERROR",
            "Data_Issue": str(e)
        })

report = pd.DataFrame(results)

report.to_csv(
    REPORT_DIR / "data_quality_report.csv",
    index=False
)

print(report.to_string(index=False))
print("\nTotal CSV files:", len(report))
print("\nReport generated successfully!")
