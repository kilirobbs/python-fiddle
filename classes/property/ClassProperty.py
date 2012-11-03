# http://stackoverflow.com/questions/128573/using-property-on-classmethods

class ClassProperty(object):
    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter
    def __get__(self, cls, owner):
        return getattr(cls, self.getter)()
    def __set__(self, cls, value):
        getattr(cls, self.setter)(value)

class MetaFoo(type):
    var = ClassProperty('getvar', 'setvar')

class Foo(object):
    __metaclass__ = MetaFoo
    _var = 5
    value=None
    @classmethod
    def getvar(cls):
        print "Getting var =", cls._var
        return cls._var
    @classmethod
    def setvar(cls, value):
        print "Setting var =", value
        cls._var = value

Foo.var=14
Foo._var=14
Foo.value=88