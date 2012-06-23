var=1488

class foo():
	def __init__(self):
		print globals()["var"]

foo()