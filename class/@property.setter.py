# http://stackoverflow.com/questions/2825452/correct-approach-to-validate-attributes-of-an-instance-of-class

#class classname(): # error

class classname(object): # object required
    _value = None

    def __init__(self,value=None):
        self.value=value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        print "setter"
        if not (v > 0):
            raise Exception("value must be greater than zero")
        self._value = v

instance = classname(14)
#instance.value = 88

#classname.value = 88
