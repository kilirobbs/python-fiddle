from shutil import copy
import sys
m = sys.modules[__name__]
copy(m.__file__,m.__file__+"2")