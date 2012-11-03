class a(object):
    pass


class b(a):
    pass


class c(b):
    pass

print c.__bases__
# (<class '__main__.b'>,)


class a_ex(object):
    pass


class d(a, a_ex):
    pass

print d.__bases__
# (<class '__main__.a'>, <class '__main__.a_ex'>)
