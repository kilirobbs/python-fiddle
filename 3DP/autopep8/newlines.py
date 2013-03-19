#!/usr/bin/env python
# -*- coding: utf-8 -*-
from autopep8 import FixPEP8

class options:
    ignore="E501"
    select = []
    verbose = False


fixed=False
contents=open(__file__).read()

while not fixed:
    f = FixPEP8(None, options(),contents=contents)
    fixed=f.fix()==contents
    contents = f.fix()
print contents
