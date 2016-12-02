#System Module
import sys
sys.stderr.write('This is stderr text\n')
sys.stderr.flush
sys.stdout.write('This is std out text\n')


#Can pass arguments when calling this file, from command line or some other place
if len(sys.argv) > 1:
    print(float (sys.argv[1])+5)
    
