class classname():
	id=None

	def method(self):
		pass

	@property
	def some_property(self):
		return 88

	@property
	def property_with_error(self):
		raise TypeError 

print hasattr(classname,"id")
print hasattr(classname,"method")
print hasattr(classname,"some_property")
print hasattr(classname,"property_with_error")