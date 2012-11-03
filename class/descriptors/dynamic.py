class RevealAccess(object):
    val = None
    name = None

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print '__get__', self.name
        return self.val

    def __set__(self, obj, val):
        print '__set__', self.name
        print 'val', val
        self.val = val


class classname(object):
    x = None

    def __init__(self):
        self.__class__.y = RevealAccess(2, "y")

    def __getattr__(self, name):
        return section(self, name)  # called if self.key not exists


instance1 = classname()
instance1.x = 1
print instance1.x
print instance1.y
instance1.y=3