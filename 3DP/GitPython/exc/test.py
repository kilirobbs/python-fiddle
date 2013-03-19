#!/usr/bin/env python
from git import exc,Repo

path="/Users/nordmenss/git/pg_test2"
try:
    repo = Repo(path)
except exc.NoSuchPathError,e:
    print type(e),str(e)
except exc.InvalidGitRepositoryError:
    repo = Repo.init(path, bare=False)
except Exception,e:
    print type(e),str(e)