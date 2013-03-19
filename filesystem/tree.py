#!/usr/bin/env python
from fnmatch import fnmatch
from os import walk
from os.path import join
from file import filter

def remove_ignored(list,ignore=[]):
    for i in ignore:
        for l in list:
            if fnmatch(l,i):
                try:
                    list.remove(l)
                except:
                    pass
    return list

def files(path,tree=False,find=["*"],ignore=[],topdown=True):
    result =[]
    for parent, _dirs,_files in walk(path,topdown=topdown):
        # remove ignored
        _dirs=remove_ignored(_dirs,ignore)
        _files=remove_ignored(_files,ignore)
        # filter by pattern
        _dirs=filter(_dirs,find)
        _files=filter(_files,find)
        for f in _files:
            result.append(join(parent,f))
        if not tree: # top level only
            return result
    return result

path="/Users/nordmenss/git/python/giturl.py"
#find=["*"]
find=["*.py"]
ignore=[".git",".DS_Store"]
result =files(path,tree=True,find=find,ignore=ignore,topdown=True)
print "\n".join(result)
