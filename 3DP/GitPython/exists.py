#!/usr/bin/env python
from git import exc, Repo
path = "/Users/nordmenss/git"
try:
    repo = Repo(path)
except exc.InvalidGitRepositoryError:
    print "not git repository"
except Exception,e:
    print type(e),str(e)
