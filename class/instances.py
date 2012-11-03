import gc

class classname():
	value=None

instance1=classname()
instance2=classname()

# http://stackoverflow.com/questions/328851/python-printing-all-instances-of-a-class

for obj in gc.get_objects():
    if isinstance(obj, classname):
        print obj