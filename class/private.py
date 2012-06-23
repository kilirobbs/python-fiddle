class Color(object):
    def __init__(self, name):
        self.__name = name # private field

    def name(self):
        return self.__name

c = Color('Red')
print c.name() 
# Red
print c._Color__name # access by  ClassName._ClassName__AttrName 
# Red

print c.__name # AttributeError: 'Color' object has no attribute '__name'