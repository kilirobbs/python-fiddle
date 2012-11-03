import os
import glob
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

for m in __all__:
    if m != "__init__":
        print m
        exec "from %s import *" % m
