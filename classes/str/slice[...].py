#!/usr/bin/env python
import os

s = "123456789"

print s[0:3]
# 123

print s[3:]
# 456789

print s[0:-1]
# 12345678

filename = "filename.sql"

print filename[:-4]
fileName, ext = os.path.splitext(filename)
print fileName

print "filename.pyc"[0:-1]
# filename.py
print "filename.pyc"[:-1]
# filename.py


print "123456789"[1:-1]

print " "[1:] is ""