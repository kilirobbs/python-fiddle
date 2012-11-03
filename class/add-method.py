# http://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object

def method(self):
	print "hello"

class classname():
	pass

classname.method=method
instance=classname()

instance.method()

