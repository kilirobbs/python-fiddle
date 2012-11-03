import glob
import os
import shutil
import sys
from distutils import dir_util

m = sys.modules[__name__]
dirname = os.path.dirname(m.__file__)
new_dirname = dirname + "/copy_tree"
# 1) distutils.dir_util.copy_tree
dir_util.copy_tree(dirname, new_dirname)

files = glob.glob("%s/*" % dirname)
new_files = glob.glob("%s/*" % new_dirname)
diff = list(set(files) - set(new_files))
print diff
#map(os.unlink,old_files)
# 2) map(shutil.copy())
#shutil.copy()
#map(lambda x: round(x, 1), L)