import shutil
import sys
m = sys.modules[__name__]
shutil.copy(m.__file__,m.__file__+"2")