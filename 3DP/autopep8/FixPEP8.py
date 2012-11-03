import autopep8, sys

# select errors / warnings (e.g. ["E4", "W"])
SELECT = []

# do not fix these errors / warnings (e.g. ["E4", "W"])
IGNORE = "E501"
IGNORE = ""


class options(object):
    def __init__(self):
        self.ignore = IGNORE
        self.select = SELECT
        self.verbose = False

options = options()

#fix = autopep8.FixPEP8(sys.modules[__name__].__file__, options)
fix = autopep8.FixPEP8(sys.modules[__name__].__file__,options,contents="import os, sys, subprocess\n")
# notice: contents must constain one \n at least
fixed = fix.fix()
if isinstance(fixed, str):
    fixed = fixed.decode('utf-8')
print fixed