from git import *

path="/Users/nordmenss/git/pg_test2"
try:
	repo = Repo(path)
except:
	repo = Repo.init(path, bare=False)