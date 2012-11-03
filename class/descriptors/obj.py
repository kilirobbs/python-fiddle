class cls(object):
    def __init__(self, initval=None, name='var'):
        self.value = initval
        self.name = name

    def __get__(self, obj, objtype):
        print '__get__', self.name
        return self.value

    def __set__(self, obj, value):
        print '__set__', self.name
        self.value = value

i = cls()
print i