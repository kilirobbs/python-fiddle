#!/usr/bin/env python
absfunc=lambda f:abs(f)
print absfunc(-1)

summ=lambda x,y:x+y
print summ(1,2)

func=lambda: 1 is not None
print func,func.__class__
print func,func()

func=lambda a,b="default": a+b
print func("_")