#!/usr/bin/env python
from git import Repo
dir="/Users/nordmenss/git/cancerhermit.github.com/"
repo = Repo(dir)
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
try:
	print repo.git.commit(m=' "my commit message"' )
except Exception,e:
	print str(e)
print repo.git.status()