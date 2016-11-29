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



try:
    whatTime = input ('What time index do you want to have lat/long for?')
    if whatTime in times:
        timeindex = times.index(whatTime)
        theLat = latitudes[timeindex]
        theLong = longitudes[timeindex]
        print (theLat, theLong)
    else:
        print('The index that you entered,', whatTime, ',is not in the list')
        
# Py 2.7 except Exception, e

except Exception as e:
    print (e)
