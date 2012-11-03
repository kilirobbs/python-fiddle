import os
import sys
from distutils import dir_util

m = sys.modules[__name__]
dirname = os.path.dirname(m.__file__)
new_dirname = dirname + "/copy_tree"
# 1) distutils.dir_util.copy_tree
dir_util.copy_tree(dirname, new_dirname)


# 2)
def copy(src, dst):
    """copy src (directory or file) to dst"""
    if os.path.exists(src):
        if os.path.isdir(src):
            dir_util.copy_tree(src, dst)

def files(directory):
    """return list of directory root files"""
    if os.path.exists(directory):
        result = []
        for parent, dirs, filenames in os.walk(directory, topdown=True):
            for name in filenames:
                filename = os.path.join(parent, name)
                result.append(filename)
            return result
    else:
        return []

def sync(src, dst):
    if os.path.isdir(src):
        src_files = files(src)
        dst_files = files(dst)
        # copy src to dst
        copy(src, dst)
        src_basenames = map(os.path.basename, dst_files)
        dst_basenames = map(os.path.basename, src_files)
        diff = list(set(src_basenames) - set(dst_basenames))
        # delete outdated files
        map(os.unlink, map(lambda x: os.path.join(dst, x), diff))