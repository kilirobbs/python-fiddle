class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.value = initval
        self.name = name

    def __get__(self, obj, objtype):
        print '__get__', self.name
        return self.value

    def __set__(self, obj, value):
        print '__set__', self.name
        self.value = value

class clasname(object):
    #x = RevealAccess(10, 'var "x"')
    x = None # RevealAccess(10, 'var "x"')
    def __init__(self):
        self.x = RevealAccess(10, 'var "x"') # dont work

instance = clasname()
instance.x
instance.x = 88