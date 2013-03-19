#!/usr/bin/env python
# -*- coding: utf-8 -*-
from glob import glob
from autopep8 import FixPEP8


class options(object):
    def __init__(self):
        self.ignore = "E501"
        self.select = []
        self.verbose = False

def autofix(f):
    source = open(f).read()  # original
    contents = source
    fixed = False
    while not fixed:
        pep = FixPEP8(None, options(), contents=contents)
        fix = pep.fix()
        fixed = fix == contents
        contents = fix
    if source != fix:
        open(f, "w").write(fix)

for f in glob("*.py"):
    autofix(f)