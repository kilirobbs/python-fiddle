#!/usr/bin/env python
from inspect import getinnerframes
from sys import exc_info
from fixtures import error
error()
try:
    error()
except:
    exc_type, exc_obj, exc_tb = exc_info()

print "getinnerframes"
for f in getinnerframes(exc_tb):
    print f#,"%s:%s" % (f[1],f[2])