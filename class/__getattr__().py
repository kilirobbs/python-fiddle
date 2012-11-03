class classname(object):
    existing = "existing"

    def __getattribute__(self, key):
    	print "__getattribute__",key
    	return object.__getattribute__(self, key)

    def __getattr__(self, key):
    	# called if self.key not exists 
        if key == "valid_name":
            return "value"
        else:
            raise AttributeError, key

print classname().existing
print classname().not_existing
