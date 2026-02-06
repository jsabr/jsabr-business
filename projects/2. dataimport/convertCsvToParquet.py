import pandas as pd
import os 


csvpath = input("Enter the path to your CSV file: ").strip()
if not os.path.isfile(csvpath):
    print(f"Error: File '{csvpath}' not found.")

parquetpath = input("Enter the output Parquet file path: ").strip()

try:

    df = pd.read_csv(csvpath)
    df.to_parquet(parquetpath, engine="pyarrow", index=False)

except Exception as e:
    print(f"An error occurred: {e}")

