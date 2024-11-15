# utils/data_utils.py
import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def append_csv(file_path, row, fieldnames):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(row)

def initialize_csv(file_path, fieldnames):
    try:
        with open(file_path, mode='x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    except FileExistsError:
        pass