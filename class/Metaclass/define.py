class BaseClass(object):
	pass

class MyClass(BaseClass):
	attribute = 42


MyClass2 = type("MyClass", (BaseClass,), {'attribute' : 42})