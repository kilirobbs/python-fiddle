import inspect,sys

print inspect.getmembers(sys.modules["inspect"], inspect.isclass)