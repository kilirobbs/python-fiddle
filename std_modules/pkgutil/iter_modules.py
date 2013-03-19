#!/usr/bin/env python
from pkgutil import iter_modules
a=iter_modules()
while True:
    try: 
        x=a.next()
        print x[0].path
    except: 
        break