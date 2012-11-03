class classname(object):
	subclass=None
	def __init__(self):
		self.subclass=set_class()

class set_class(object):
	def __get__(self):
		print "__get__"
	def __set__(self):
		print "__set__"

i=classname()
i.subclass