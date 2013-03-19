from os.path import dirname, expanduser, join
from os import walk


def files(dir):
    """list of directory top level files"""
    return map(lambda x:join(dir,x),next(walk(expanduser(dir)))[2])

str_files=files(dirname(__file__))
unicode_files=files(dirname(__file__).decode("utf-8"))
for f in unicode_files:
    print f,f.__class__