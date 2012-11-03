import csv
import os
filename = os.path.expanduser("~/.pgpass")
data = csv.reader(open(filename),
                  delimiter=':',
                  escapechar='\\'
                  )
print data.next()
print data.next()
print data.next()
print data.next()
print data.next()