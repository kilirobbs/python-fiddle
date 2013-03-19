#!/usr/bin/env python
from os import unlink,symlink
from os.path import exists,islink,isfile,realpath

l=__file__+"(link)"
if exists(l):
    unlink(l)
symlink(__file__,l)
print "isfile=",isfile(l)
print "islink=",islink(l)

l="/usr/share/git-core/templates/HEAD"
print "isfile=",isfile(l)
print "islink=",islink(l)

print realpath("~/.gitconfig")