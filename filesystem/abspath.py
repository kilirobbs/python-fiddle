#!/usr/bin/env python
from os.path import abspath,basename,dirname,isabs

print abspath(basename(__file__))
print isabs(__file__),isabs("../")
print abspath("../")

print basename(__file__)