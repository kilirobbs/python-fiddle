class classname(): # wrong
	pass

class classname(object):
	pass

class sub_classname(classname):
	pass

print classname.__subclasses__
print classname.__subclasses__()