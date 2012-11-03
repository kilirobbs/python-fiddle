def attributes(obj):
    import types
    MethodWrapperType = type(object().__hash__)
    methods = []
    builtins = []
    classes = []
    attrs = []
    for slot in dir(obj):
        attr = getattr(obj, slot)
        if slot in ['__class__', '__doc__', '__module__']:
            pass
        elif (isinstance(attr, types.BuiltinMethodType) or
              isinstance(attr, MethodWrapperType)):
            builtins.append(slot)
        elif (isinstance(attr, types.MethodType) or
              isinstance(attr, types.FunctionType)):
            methods.append((slot, attr))
        elif isinstance(attr, types.TypeType):
            classes.append((slot, attr))
        else:
            attrs.append(slot)
    return attrs


class classname(object):
    value = None
print attributes(classname())
