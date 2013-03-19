#!/usr/bin/env python
from os.path import dirname

print dirname("justfilename")
path = "schema/public/table/tablename/index/indexname.md"
dirname = dirname(path)
print dirname
print dirname.split("/")
print dirname.split("/")[-1]

from os.path import abspath, dirname, join
readme = join(dirname(abspath(__file__)),'README.rst')