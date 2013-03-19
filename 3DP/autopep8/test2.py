#!/usr/bin/env python
from autopep8 import FixPEP8


class options(object):
    def __init__(self):
        self.ignore = "E501"
        self.select = []
        self.verbose = False

f = FixPEP8(__file__, None)
fixed = f.fix()
if isinstance(fixed, str):
    fixed = fixed.decode('utf-8')
print fixed, fixed.__class__
