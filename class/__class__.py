class example():
	value=None

class example2(example):
	pass

	def func(self):
		print "subchild method"

instance=example()
instance.__class__=example2
instance.func()