class classname(object):
    existing = "existing"
    
    def __setattr__(self, k,v):
        print "__setattr__"
        if hasattr(self,k):
            print "%s exists" % k
            super(classname, self).__setattr__(k, v)
        else:
            print "%s not exists" % k 

classname().existing=88
print ""
classname().id=88
