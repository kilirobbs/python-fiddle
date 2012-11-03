import sys
class module_cls(sys.modules[__name__].__class__,object):
    def __getattribute__(self,k):
        print k
print sys.modules
sys.modules.update(dict(__main__=module_cls(__name__)))
print sys.modules