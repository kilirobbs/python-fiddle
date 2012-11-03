class classname(object):
    id = None
    value = None

    def __init__(self, **kwargs):
        while len(kwargs) > 0:
            setattr(self, kwargs.keys()[0], kwargs.pop(kwargs.keys()[0]))

instance = classname(**dict(id=14, value="title"))
print instance.id
print instance.value