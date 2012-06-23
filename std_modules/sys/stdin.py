import sys

# http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python

for line in sys.stdin:
    print line

name = raw_input("Enter your name: ")