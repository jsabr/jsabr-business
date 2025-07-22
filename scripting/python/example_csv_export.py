import csv

# Example data
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
]

# Define the CSV file name
filename = "people.csv"

# Writing to CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader()  # Write column names
    writer.writerows(data)  # Write data rows

print(f"Data exported to {filename}")