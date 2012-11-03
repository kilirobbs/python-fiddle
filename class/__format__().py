class example():
	value=None

	def __format__(self,value):
		print "__format__"
		return value


print "{:%d.%m.%Y}".format(example()) # call __format__
print example().__format__("%d.%m.%Y") # same as