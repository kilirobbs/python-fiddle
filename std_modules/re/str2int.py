#!/usr/bin/env python
# http://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string-in-python

from re import findall

def str2int(value):
	matches=findall("[-+]?\d+", value)
	if len(matches)>0:
		return int(matches[0])
	else:
		return None


print str2int("Current Level: -13.4 db.")
print str2int("test")

s="14 last message repeated 88 time"
print findall("[-+]?\d+", s[20:])

print findall("\[\d+\]", "14[88]")