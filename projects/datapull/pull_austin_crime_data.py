import pandas as pd
import requests

params = {
    '$where': "occ_date > '2024-12-01'",  # Very narrow date range
    '$limit': 1000  # Small batch
}
response = requests.get("https://data.austintexas.gov/resource/fdj4-gpfu.csv", params=params)
df_sample = pd.read_csv(pd.io.common.StringIO(response.text))

df = pd.DataFrame.from_records(df_sample)

df.to_csv("crime_sample.csv", index=False)
