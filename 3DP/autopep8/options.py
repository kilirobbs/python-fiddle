#!/usr/bin/env python
from autopep8 import FixPEP8

class options:
    ignore="E501"
    select = []
    verbose = False
    max_line_length=79
    aggressive=True

f = FixPEP8(__file__, options())
fixed = f.fix()
print fixed
