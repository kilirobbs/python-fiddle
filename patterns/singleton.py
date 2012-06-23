class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
             cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
 
a = Singleton()
b = Singleton()
a is b

print Singleton.instance
# <__main__.Singleton object at 0x107ad5390>