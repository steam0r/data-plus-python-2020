import csv

csv_file = open('time_series_covid19_recovered_global.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count == 0:
        cell_count = 0
        for col in row:
            print("Name Spalte:", cell_count, col)
            cell_count += 1
    line_count += 1
print("Zeilen in Datei:", line_count)