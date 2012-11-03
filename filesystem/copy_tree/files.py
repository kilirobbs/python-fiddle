import os
import fnmatch
import time

path = "/Users/nordmenss/git/pg_test"


def files_with_pattern(directory, pattern='*'):
    result = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                result.append(filename)
    return result


def files_iterator(path):
    for parent, dirs, files in os.walk(path,topdown=True):
        try:
            dirs.remove('.git')
        except ValueError:
            pass
        for filename in files:
            path, ext = os.path.splitext(filename)
            if ext in [".oid", ".sql", ".preferences"]:
                yield os.path.join(parent, filename)


def files_list(path, ignore=None):
    result = []
    for parent, dirs, files in os.walk(path,topdown=True):
        try:
            dirs.remove('.git')
        except ValueError:
            pass
        for filename in files:
            result.append(os.path.join(parent, filename))
    return result

t = time.time()
files = files_with_pattern(path,"^[git]")
for f in files:
    print f
print "files_with_pattern : %f" % (time.time() - t)

t = time.time()
print "\n\nstart files_iterator"
for f in files_iterator(path):
    #print f
    pass
print "files_iterator : %f" % (time.time() - t)
t = time.time()
print "\n\nstart files_list"
files = files_list(path)
files = map(lambda x:x.replace(path+"/",""),files)
for f in files:
    print f
print "files_list : %f" % (time.time() - t)
