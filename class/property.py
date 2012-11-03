class Foo():
	value=None
	def __init__( self, value ):
		self.value=value
	@property
	def bar(self):
		return self.value+"_Foo"

class FooBar(Foo):
	@property
	def bar(self):
		return self.value+"_FooBar"
		return Foo.bar(self)

ins=Foo(value="1488")
print ins.bar