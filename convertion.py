import csv
import os

# Directory containing your .txt files
txt_directory = './data/marker_data/ab05/Walk/Slow'  # Replace with your directory containing .txt files
csv_directory = './data/marker_data/ab05/Walk/Slow'  # Replace with your directory to save .csv files

# Check if the output directory exists, create if not
if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

txt_files = [f for f in os.listdir(txt_directory) if f.endswith('.txt')]

for txt_file in txt_files:
    with open(os.path.join(txt_directory, txt_file), 'r') as file:
        lines = file.readlines()

        # Parsing tab-separated values into separate columns
        data_columns = [line.strip().split('\t') for line in lines]

        # Writing to .csv file
        csv_file = os.path.join(csv_directory, os.path.splitext(txt_file)[0] + '.csv')
        with open(csv_file, 'w', newline='') as csv_output:
            writer = csv.writer(csv_output)
            writer.writerows(data_columns)
