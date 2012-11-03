class RevealAccess(object):
    value=None
    def __get__(self, obj, objtype):
        print "__get__ from obj",obj.id,objtype
        return self.value

    def __set__(self, obj, value):
        print "__set__ obj",obj.id
        self.value = value

class classname(object):
    x = RevealAccess() 
    id = None
    def __init__(self,id):
        self.id=id

    def __getattribute__(self, k):
        try:
            # super(self.__class__,self)# max recursive
            return super(classname,self).__getattribute__(k)
        except AttributeError: # not exists
            pass

instance = classname(1)
instance.x = 88
print instance.x
classname.x=14 # instance only