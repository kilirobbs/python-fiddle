# http://www.ibm.com/developerworks/ru/library/l-pymeta/

def meta(name):
    class cls():
        pass

    cls.__name__ = name
    return cls

new_class=meta("new_class1")
print new_class.__name__