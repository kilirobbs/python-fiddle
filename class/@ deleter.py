class classname(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


    @x.deleter
    def x(self):
        print "deleter"
        del self._x

instance = classname()
del instance.x