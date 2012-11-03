import os
from git import *

def hashes(path):
	result=[]
	repo = Repo(path)
	for commit in repo.iter_commits(repo.head.reference, max_count=-1, skip=-1):
		result.append(commit.hexsha)
	return result

print hashes("/Users/nordmenss/git/pg_test")