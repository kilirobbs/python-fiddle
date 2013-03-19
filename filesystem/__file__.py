#!/usr/bin/env python
from os.path import dirname,join,relpath

print __file__
print dirname(__file__)
print join(dirname(dirname(__file__)),"subdir")
print relpath(__file__,"../")