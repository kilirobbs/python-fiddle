import os

path = "schema/public/table/tablename/index/indexname"
dirname = os.path.dirname(path)
print dirname

print dirname.split("/")[-1]

from os.path import abspath, dirname, join
readme = join(dirname(abspath(__file__)),'README.rst')