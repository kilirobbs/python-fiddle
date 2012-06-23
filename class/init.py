class Circle():
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)



c=Circle(name="name",value="value")
print c.name