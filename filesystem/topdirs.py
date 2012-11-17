from os.path import basename, dirname, expanduser, join
from os import walk

path = dirname(__file__)
print path


def topdirs(dir):
    """list of directory top level files"""
    return map(lambda x:join(dir,x),next(walk(dir))[1])


def dirs(path):
    result=[]
    for d in topdirs(path):
        if basename(d)!=".git":
            result.append(d)
            result+=dirs(d)
    return result

#print "\n".join(topdirs(path))
print dirs(expanduser("~/git/bash-profile"))