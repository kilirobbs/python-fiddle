from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
try:
	print repo.git.commit(m='my commit message' )
except:
	pass
print repo.git.status()