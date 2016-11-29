import csv

with open('aCSVFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    latitudes = []
    longitudes = []

    for row in readCSV:
        latitude = row[2]
        longitude = row[3]
        latitudes.append(latitude)
        longitudes.append(longitude)

print (latitudes)
print (longitudes)
