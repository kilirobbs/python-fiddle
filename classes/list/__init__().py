#!/usr/bin/env python
import __builtin__

class sublist(list):
    def __init__(self, data=[]):
        #super(type(self),self).__init__(data)
        __builtin__.list(self).__init__(data)

l = sublist([1, 2])
print l.items()
