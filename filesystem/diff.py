from os.path import dirname, join
from os import walk

path = dirname(__file__)
print path

def files(dir):
    """list of directory root files"""
    return map(lambda x:join(dir,x),next(walk(dir))[2])

print "\n".join(files(path))