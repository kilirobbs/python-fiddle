# http://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string-in-python

import re

def str2int(value):
	matches=re.findall("[-+]?\d+", value)
	if len(matches)>0:
		return int(matches[0])
	else:
		return None


print str2int("Current Level: -13.4 db.")
print str2int("test")