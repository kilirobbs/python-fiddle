import os.path

# http://docs.python.org/library/os.path.html#os.path.expanduser

print os.path.abspath(__file__)
# /Users/nordmenss/git/python-overview/modules/os/path.py


print os.path.basename(__file__)
# path.py

print os.path.commonprefix([__file__,__file__,__file__])
# /Users/nordmenss/git/python-overview/modules/os/path.py

print os.path.dirname(__file__)
# /Users/nordmenss/git/python-overview/modules/os

print os.path.exists(__file__)
# True

print os.path.expanduser("~")
# /Users/nordmenss

print os.path.getatime(__file__) # Return the time of last access of path.
# 1337535637.0

os.path.getmtime(__file__) # Return the time of last modification of path. 

print os.path.getsize(__file__) # size

print os.path.isabs(__file__) # Return True if path is an absolute pathname.
# True
print os.path.isabs("~")
# False

print os.path.isfile(__file__)
print os.path.isdir(__file__)
print os.path.islink(__file__)
print os.path.ismount(__file__)