import csv

with open('aCSVFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        print (row[0])
        print (row[0], row[1])
