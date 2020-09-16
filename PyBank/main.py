import os
import csv
csv_path=os.path.join("resources","budget_data.csv")
with open (csv_path) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    print(csv_reader)

