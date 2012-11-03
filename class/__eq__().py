class version():
    _start = None
    _end = None

    def __init__(self,start,end=None):
        self.start=start
        self.end=end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, v):
        if isintance(v,(int,float)):
            self._start=v
        else:
            raise TypeError("Invalid version, expected int/float")

    @property
    def end(self):
        return self._start

    @end.setter
    def end(self, v):
        if isintance(v,(int,float)):
            self._end=v
        else:
            raise TypeError("Invalid version, expected int/float")

    def __eq__(self,v):
        if isinstance(v,(int,float)):
            if self.end:
                return self.start<=v<=self.end
            else:
                return self.start<=v
        else:
            raise TypeError("int/float expected")

print version(7.3,9.2)==8.0
print version(7.3,9.2)==9.3
print version(7.3)==9.3