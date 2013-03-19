#!/usr/bin/env python
# http://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string-in-python

from re import findall
print findall("\d+.\d+", "Current Level: 13.4 db.")[0]