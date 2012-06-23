# http://docs.python.org/tutorial/classes.html

class Base():
	def __init__(self):
		print "Constructor A was called"

	def echo(self):
		print "base"

class Base_ex(Base):
	def __init__(self):
		Base.__init__(self)
		# super(Base_ex, self).__init__()
		# super().__init__() # PYTHON 3
		print "Constructor B was called"


	def echo(self):
		print "base_ex"

	def base_echo(self):
		Base.echo(self) # call class method by name

for base_class in Base_ex.__bases__:
	print base_class
# __main__.base

x=Base()
x.echo()
# base

y=Base_ex()

y.base_echo()
# base
print ""
for attr in y.__class__.__bases__[0].__dict__:
    print attr

