import os
filename=os.path.expanduser("~/.pgpass")
# mode string must begin with one of 'r', 'w', 'a' or 'U'
print open(filename,"r").mode
print open(filename,"w").mode
print open(filename,"r").mode
print open(filename,"a").mode
print open(filename,"aaaaaaaa").mode

import StringIO
try:
	print StringIO.StringIO().mode
except:
	print "error"
