class class1(object):
    value=None

class class2(object):
    value=None

class class3(object):
    value=None

#class multiclass(object,class1,class2,class3): # Wrong - TypeError: Error when calling the metaclass bases Cannot create a consistent method resolution
# TypeError: Error when calling the metaclass bases
# Cannot create a consistent method resolution
class multiclass(class1,class2,class3,object):
	def __init__(self):
		self.value=88

obj=multiclass()
print obj.value