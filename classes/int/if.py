#!/usr/bin/env python
value=-10
if value:
	print "True"
else:
	print "False"

if value is None:
    print "None"
else:
    print "not None"

zero=0
print zero
print not zero
print isinstance(zero,int)
print isinstance(None,int)