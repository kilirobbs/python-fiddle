import os
h = open(os.path.expanduser("~/.pgpass"), "r")
i = 2
l = h.readlines()
print l
l.pop(2)
print "".join(l)