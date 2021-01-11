import os
import csv

Output_path = os.path.join("..", "analysis", "new.csv")

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")

    #For row in csvreader:

