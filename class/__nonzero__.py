class classname():
    value = None

    def __init__(self, value):
        self.value = value

    def __nonzero__(self):
        return self.value

if classname(True):
    print "nonzero"
else:
    print "zero"

if classname(False):
    print "nonzero"
else:
    print "zero"
