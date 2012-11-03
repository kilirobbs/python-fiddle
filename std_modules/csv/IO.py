import csv
import os
from StringIO import StringIO
reader = csv.reader(StringIO(":".join(["*"]*5)),
                    delimiter=':',
                    escapechar='\\')
for r in reader:
    if r and not r[0].strip().startswith('#'):
        print r  # , r[-1].split("#")
    if r:
        print "valid"
    else:
        print "invalid"
