import os
import glob

# import all files
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
for m in __all__:
    module = __import__("pgit")
print module, module.__file__
