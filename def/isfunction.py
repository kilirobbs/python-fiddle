from inspect import isfunction
from types import FunctionType

def f(): pass
print isfunction(f)
print FunctionType==f.__class__
print hasattr(f, '__call__')