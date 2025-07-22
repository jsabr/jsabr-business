import pandas as pd

# Example data as a list of dictionaries
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Export to CSV
df.to_csv("people.csv", index=False)  # index=False prevents writing row numbers

print("CSV exported as 'people.csv'")
