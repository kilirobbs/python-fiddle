# http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
# Difference between __str__ and __repr__ in Python

class classname(object):
	value=None
	def __init__(self,value="default"):
		self.value=value

	def __str__(self):
		return self.value

	def __repr__(self):
		return "%s(%r)" % (self.__class__, self.__dict__)

print "repr(classname())=",repr(classname())
print "str(classname())=",str(classname())
print "%s" % classname()
print "classname()=",classname()