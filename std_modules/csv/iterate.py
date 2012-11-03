import csv
import os
filename = os.path.expanduser("~/.pgpass")
reader = csv.reader(open(filename),
                    delimiter=':',
                    escapechar='\\')

print list(reader)

reader = csv.reader(open(filename),
                    delimiter=':',
                    escapechar='\\')
for r in reader:
    print r
#if r and not r[0].strip().startswith('#'):
    #print r  # , r[-1].split("#")
#if r:
    #print "valid"
#else:
    #print "invalid"