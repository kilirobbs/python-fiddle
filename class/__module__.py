import sys

class classname():
	pass

print classname.__module__, classname.__module__.__class__
# __main__ <type 'str'>

print sys.modules[classname.__module__].classname