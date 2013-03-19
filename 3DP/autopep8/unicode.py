#!/usr/bin/env python
# -*- coding: utf-8 -*-
from autopep8 import FixPEP8

class options:
    ignore="E501"
    select = []
    verbose = False
    max_line_length=79
    aggressive=False

contents=u"""
import os, sys
print u"юникод"
"""

fix = FixPEP8(__file__, options, contents=contents)
fixed = fix.fix()
print fixed