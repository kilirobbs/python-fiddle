# http://stackoverflow.com/questions/5701201/using-unbound-methods-in-another-python-class

class foo:
    def ops(self, name):
        print "Hi there",name

foo().ops("Peter")

class foo2:
    pass

foo2.ops = foo.ops.im_func

foo2().ops('Alice')