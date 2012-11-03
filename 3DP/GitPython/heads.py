from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
heads=repo.heads
print "repo.heads=",heads
master = repo.heads.master # access by name
print master.commit # last commit 

