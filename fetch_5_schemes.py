
import requests
import pandas as pd
import os

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

os.makedirs("data/raw", exist_ok=True)

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(data["data"])

        df["scheme_name"] = data["meta"]["scheme_name"]
        df["amfi_code"] = code

        filename = f"data/raw/{name}_nav.csv"

        df.to_csv(filename, index=False)

        print(f"{name}: Downloaded {len(df)} records")

    except Exception as e:
        print(f"{name}: ERROR - {e}")

print("\nAll scheme downloads completed!")
