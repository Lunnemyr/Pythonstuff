# Tuples are faster than lists and can not be changed!
x = 5,6,2,6
y = (5,6,2,6)

# List
z = [5,6,2,6]


def exampleFunc():
    return 15,6

a,b = exampleFunc()

print (a)
print (b)
