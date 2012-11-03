class classname():
	id=None
	l=[]
	def __init__(self,id):
		self.id=id
		self.l.append(1)
		self.l.append(2)

i=classname(88)
setattr(i,"id",1488)
print getattr(i,"id")

getattr(i,"l").append(3)
print getattr(i,"l")
# [1, 2, 3]