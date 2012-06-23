class example():
	"""A simple example class"""
	items=[]
	def __init__(self,key=None,**kwargs): # initialize
	    self.data = []
	    for key, value in kwargs.iteritems():
			setattr(self, key, value)

	def __del__(self): # desctuctor
	    self.data = []

	def __hash__(self):
		pass

	def __nonzero__(self): # used in if. while
		return len(self.items)>0

	def __getitem__(self,key): # return object[key]
		return self.items[key]

	def __setitem__(self,key,value): # set object[key]=value
		 self.items[key]=value

	def __delitem__(self,key): # del object[key]
		del self.items[key]

	def __getslice__(self,key): # 
		pass

	def __setslice__(self,key): # 
		pass

	def __delslice__(self,key): # 
		pass

	def __contains__(self,item): # item in object / item not in object
		pass 

	def __repr__(self):
		return "<example('%s')>" % self.items

	def __complex__(self):
		pass

	def __int__(self):
		pass

	def __long__(self):
		pass

	def __float__(self):
		pass

	def __neg__(self):
		pass

	def __pos__(self):
		pass

	def __invert__(self):
		pass

	def __abs__(self):
		pass

	def get(self,key):
		return self.__getattr__(key) # get value by name

	def set(self,key,value):
		return self.__setattr__(key,value) # set value by name

	def f(self):
		return 'hello world'

	@staticmethod
	def statis_method_only(self):
		pass


print example.__dict__ # attributes dict
# {'i': 12345, '__module__': '__main__', '__doc__': 'A simple example class', '__init__': <function __init__ at 0x104bcf140>, 'f': <function f at 0x104bcf758>}

print example.__module__ # module name where class if defined
# __main__

print example.__name__
# example

print example.__bases__ # base classes 
# ()

print example.__doc__
# A simple example class

# print example.__file__

print example() # __repr__
# <example('12345')>

if example(): # __nonzero__
	print "if"