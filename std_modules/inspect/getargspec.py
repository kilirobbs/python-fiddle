#!/usr/bin/env python
def lazy_init(init):
    import inspect
    arg_names = inspect.getargspec(init)[0]

    def new_init(self, *args):
        for name, value in zip(arg_names, args):
            setattr(self, name, value)
        init(self, *args)

    return new_init

class Person:
    @lazy_init
    def __init__(self, name, age):
        pass

p = Person("Derp", 13)
print p.name