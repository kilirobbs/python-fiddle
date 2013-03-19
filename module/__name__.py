from sys import modules
print __name__
print modules[__name__].__class__
print modules[__name__].__file__