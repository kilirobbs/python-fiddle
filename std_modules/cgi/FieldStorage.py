#!/usr/bin/env python
from cgi import FieldStorage

args = FieldStorage(fp=None, headers=None,environ=dict(key="value"))
print args.keys()
for a in args.keys():
    print args[i].name,args[i].value