class classname():
    key = None
    db = "db"

    def __init__(self, key):
        self.key = key

    def __setitem__(self, key, value):
        print "__setitem__(%s)" % key


instance = classname(88)
instance["test"] = 88
