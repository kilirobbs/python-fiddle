#!/usr/bin/env python
class cls1:
    def func1(self):
        print "func1"

class cls2:
    def func2(self):
        print "func1"

class cls(cls1,cls2):
    pass


i=cls()
  i.func1(),i.func2()