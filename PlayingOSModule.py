#OS Module
import os
curDir = os.getcwd()
print (curDir)

os.mkdir('newDir')


import time
time.sleep(5)

os.rename('newDir', 'newDir2')

time.sleep(5)

os.rmdir('newDir2')


