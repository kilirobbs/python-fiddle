class classname:
    key1=None
    key2=None
    key3=None

print classname.__dict__
del classname.key1
print classname.__dict__
del classname.__dict__["key2"]
print classname.__dict__