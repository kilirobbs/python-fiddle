import sys, inspect
from inspect import *

class classname():
	pass

def all_classes(module):
	return inspect.getmembers(module, inspect.isclass)

def classes(module): # module_only_classes
	return [cls for name, cls in getmembers(module, isclass) 
		if cls.__module__ == module.__name__]

print "sys only classes:", classes(sys)
print "inspect only classes:", classes(inspect)

print "__name__ all classes: ",all_classes(sys.modules[__name__])