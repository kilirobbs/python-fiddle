from copy import copy, deepcopy

class classname1():
	value=None
	def method1(self):
		pass

	def __repr__(self):
		return "repr"

class classname2():
	pass

def get_class_members(klass):
    ret = dir(klass)
    if hasattr(klass,'__bases__'):
        for base in klass.__bases__:
            ret = ret + get_class_members(base)
    return ret

print get_class_members(classname1)

classname2.__repr__=classname1

ins=classname1()
print ins

