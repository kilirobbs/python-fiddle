import os
import shutil
import sys
from distutils import dir_util

m = sys.modules[__name__]
dirname = os.path.dirname(m.__file__)
# 1) distutils.dir_util.copy_tree
dir_util.copy_tree(dirname, dirname + "/copy_tree")

files = glob.glob("%s/*" % dirname)
print files
#map(os.unlink,old_files)
# 2) map(shutil.copy())
#shutil.copy()
#map(lambda x: round(x, 1), L)