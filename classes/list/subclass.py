#!/usr/bin/env python
class sublist(list):
    def __init__(self, data=[]):
        super(type(self), self).__init__(data)

    def __getslice__(self, i, j):
        print "__getslice__"
        return sublist(list.__getslice__(self, i, j))

    def items(self):
        return self[:]

        IndexError

l = sublist([1, 2])
print l.items()



class cls(object):
    def __init__(self,reference):
        pass 
