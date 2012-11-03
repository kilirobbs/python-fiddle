import sys
import os
from inspect import *
from pgit.postgresql.cls import *
import pgit


def module_classes(module):
    return [cls for name, cls in getmembers(module, isclass) if cls.__module__ == module.__name__]


def pkg_classes(package):
    result = []
    for file in package.__all__:
        name = "%s.%s" % ( package.__name__, file )
        if name in sys.modules:
            result += module_classes(sys.modules[name])
    return result

print pkg_classes(pgit.postgresql.cls)
