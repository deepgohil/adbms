import csv

# Specify the input and output file paths
input_csv_file = "train_file.csv"
output_csv_file = "filtered_output_file.csv"

# List of column names to keep
columns_to_keep = ["ID", "LICENSE ID", "ACCOUNT NUMBER", "SITE NUMBER"]

try:
    with open(input_csv_file, mode='r', newline='') as input_file, \
            open(output_csv_file, mode='w', newline='') as output_file:

        # Create CSV readers and writers
        csv_reader = csv.DictReader(input_file)
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(output_file, fieldnames=columns_to_keep)

        # Write the header row to the output file
        csv_writer.writeheader()

        # Iterate through each row in the input CSV and write selected columns to the output CSV
        for row in csv_reader:
            filtered_row = {column: row[column] for column in columns_to_keep}
            csv_writer.writerow(filtered_row)

    print(f"Filtered CSV file saved to {output_csv_file}")

except FileNotFoundError:
    print("File not found. Please check the file paths.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
