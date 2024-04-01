import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def compare_rows(row1, row2):
    diff = []
    for key in row1.keys():
        if row1[key] != row2[key]:
            diff.append(f"{key}: {row1[key]} != {row2[key]}")
    return diff

def find_differences(data1, data2):
    differences = []
    for row1 in data1:
        found = False
        for row2 in data2:
            if row1['Date'] == row2['Date'] and row1['Received Quantity'] == row2['Received Quantity'] and row1['Received Currency'] == row2['Received Currency'] and row1['Sent Quantity'] == row2['Sent Quantity'] and row1['Sent Currency'] == row2['Sent Currency']:
                found = True
                break
        if not found:
            differences.append(row1)
    return differences

def print_differences(differences):
    for i, row in enumerate(differences, 1):
        print(f"Difference {i}:")
        for key, value in row.items():
            print(f"{key}: {value}")
        print()

# Read the CSV files
output_data = read_csv('output.csv')
export_data = read_csv('export_cointracker.csv')

# Find the differences
output_only_rows = find_differences(output_data, export_data)
export_only_rows = find_differences(export_data, output_data)

# Print the differences
print("Rows only in output.csv:")
print_differences(output_only_rows)

print("Rows only in export_cointracker.csv:")
print_differences(export_only_rows)