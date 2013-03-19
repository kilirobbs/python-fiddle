#!/usr/bin/env python
from re import sub
from datetime import datetime
print sub("[^\d]", "_",str(datetime.now())[0:18])
print sub("[^\w]", "_","http://www.site88.com/path/?erer")

print sub("[\[\d\]]", "","label[1488]")