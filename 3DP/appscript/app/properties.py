#!/usr/bin/env python
from appscript import app,reference

print app('Terminal').properties()
try:
    print app('iTunes').properties()
except reference.CommandError,e:
    print type(e),str(e)

