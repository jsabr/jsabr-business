import pandas as pd

# Check memory usage as you go
df_sample = pd.read_csv('g_inventor_disambiguated.tsv', sep='\t', encoding='utf-8')
#                 usecols=['inventor_city', 'inventor_state', 'patent_date', 'patent_number'])


df = pd.DataFrame.from_records(df_sample)

df.to_csv("patent_inventor_sample.csv", index=False)
#print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")