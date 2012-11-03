# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

class A(object):
	value=None
	def __init__(self,value):
		self.value=value

	def foo(self,x):
		print "executing foo(%s,%s)"%(self,x)

	@classmethod
	def classmethod(cls,x):
 		print cls.value
		print "classmethod(%s,%s)"%(cls,x)
	@staticmethod
	def staticmethod(x):
		print "staticmethod(%s)"%x    

a=A(88)

a.foo(1)

a.classmethod(1)

A.staticmethod(1)