class classname():
	id=None
	l=[]
	def __init__(self,id):
		self.id=id
		self.l.append(1)
		self.l.append(2)

i=classname(88)
print getattr(i,"id")
print getattr(i,"l")[0]