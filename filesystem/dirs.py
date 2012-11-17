from os.path import basename, exists, expanduser, islink, join, realpath
from os import symlink, walk, unlink

def dirs(directory):
    """return list of nested directories"""
    result = []
    if exists(directory):
        for parent, dirs, files in walk(directory, topdown=True):
            for dir in dirs:
                result.append(join(parent, dir))
    return result