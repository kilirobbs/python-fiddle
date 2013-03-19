#!/usr/bin/env python
from os.path import basename, splitext
print splitext(".ext")
print splitext("file.ext")
print basename(splitext("gtd")[0])
print basename(splitext("/path/to/gtd")[0])