from os.path import dirname, expanduser, join
from os import walk

def files(directory):
    result = []
    for root, dirs, files in walk(directory):
        for name in files:
            f = join(root, name)
            result.append(f)
    return result

print "\n".join(files(dirname(__file__)))