class classproperty(property):
    def __get__(self, obj, type_):
        return self.fget.__get__(None, type_)()

    def __set__(self, obj, value):
        cls = type(obj)
        print "__set__"
        return self.fset.__get__(None, cls)(value)

class A (object):

    _foo = 1

    @classproperty
    @classmethod
    def foo(cls):
        return cls._foo

    @foo.setter
    @classmethod
    def foo(cls, value):
        cls.foo = value


A.foo = 10