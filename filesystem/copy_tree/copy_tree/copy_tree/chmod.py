import sys
import os


filename = sys.modules[__name__].__file__
# http://docs.python.org/library/os.html#os.chmod
os.chmod(filename,0755)