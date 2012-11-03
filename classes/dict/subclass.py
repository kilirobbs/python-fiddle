# http://stackoverflow.com/questions/2060972/subclassing-python-dictionary-to-override-setitem

class hacked_dict(dict):
	def __init__(self, *args, **kwargs):
		self.update(*args, **kwargs)

	def __getitem__(self, key): 
		if key in self.keys():
			return dict.__getitem__(self, key)
		else:
			print "not exists"

	def __setitem__(self, key, value):
		print "__setitem__ ",key,"=",value
		super(hacked_dict, self).__setitem__(key, value)

	def values(self,keys=None):
		if keys:
			return dict((key,value) for (key,value) in self.iteritems() if key in keys)
		else:
			return super(self.__class__,self).values()

d=hacked_dict({1:"one",2:"two",3:"three"})
print d.values()
print d.values([1,2])

print d[1]

d[14]=88


