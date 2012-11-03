try:
    setattr(object(), "id", 88)
except:
    print "setattr(build-in class) error"

class classname(object):
    pass

try:
    setattr(classname(), "id", 88)
    print "setattr(my class) OK"
except:
    pass