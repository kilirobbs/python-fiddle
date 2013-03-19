#!/usr/bin/env python
x = "Hello World!"
print x[2:]
# llo World!

print x[:2]
# He 
print x[:-2]
# Hello Worl

print x [-2:]
# d!


path="pg_catalog.pg_proc.oid"
print ".".join(path.split(".")[0:-1])