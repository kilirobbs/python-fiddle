class C(object):
    pass # No methods... yet

def foo(self,instance):
    print self
    print instance

C.foo = foo
c=C()
c.foo(int) # None


import types
instance = C()
instance.bar = types.MethodType(foo, instance, instance.__class__)