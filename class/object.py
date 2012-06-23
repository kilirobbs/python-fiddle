class example():
	i=None
	l=list
	def __init__(self): # initialize
		self.data = []

x=example()

def printVars(object):
    for i in [v for v in dir(object) if not callable(getattr(object,v))]:
    	print '%s' % i.__class__

printVars(x)