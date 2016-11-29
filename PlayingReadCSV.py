import csv

with open('aCSVFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    latitudes = []
    longitudes = []
    times = []

    for row in readCSV:
        time = row[1]
        latitude = row[2]
        longitude = row[3]
        times.append(time)
        latitudes.append(latitude)
        longitudes.append(longitude)

print (latitudes)
print (longitudes)

whatTime = input ('What time index do you want to have lat/long for?')
timeindex = times.index(whatTime)

print (timeindex)

theLat = latitudes[timeindex]
theLong = longitudes[timeindex]

print (theLat, theLong)
