class classname(object):
    existing = "existing"

    def __getattribute__(self, key):
        print "__getattribute__", key
        try:  # exists
            return super(classname, self).__getattribute__(key)
        except AttributeError, e:  # not exists
            pass
        except Exception, e:
            print "not existing"
            print type(e), str(e)

ins = classname()
ins.existing
hasattr(ins, "existing")  # call __getattribute__
ins.not_existing
ins.func()
