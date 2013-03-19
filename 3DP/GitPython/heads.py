#!/usr/bin/env python
from git import Repo
repo = Repo("/Users/nordmenss/git/python/PyDefaults")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
heads=repo.heads
print "repo.heads=",heads
for head in heads:
    print head.name,head.default
master = repo.heads.master # access by name
print master.commit # last commit 

