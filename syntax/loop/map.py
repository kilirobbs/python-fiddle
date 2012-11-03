def func(value):
	print value

map(func,[1,2,3])


class classname():
	value=None
	def __init__(self,value):
		self.value=value

l=[classname(1),classname(2),classname(3),classname(4)]

print map(lambda x: x.value, l)


map(None,[1,2,3])