# Keys and values
# No order in a dictionary

exDict = {'Jack':[15, 'blonde'], 'Bob':[22,'brown'], 'Alice':[12,'black'], 'Kevin':[17, 'red']}

print (exDict)
print (exDict['Jack'])

exDict['Tim'] = 14
print (exDict)

exDict['Tim'] = 15
print (exDict)

del exDict['Tim']
print('Tim died')
print (exDict)

print (exDict['Jack'][1])
