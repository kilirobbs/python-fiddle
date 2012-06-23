class AttributeInitType(type):
  def __call__(self, *args, **kwargs):
    """ return new object """
    # first, create object...
    obj = type.__call__(self, *args)
    for name in kwargs:
      setattr(obj, name, kwargs[name])
    return obj

class Man(object):
   __metaclass__ = AttributeInitType

me = Man(height = 180, weigth = 80)
print me.height