import os
from git import *

def files(hash):
	class git_files_list():
		result=[]
		def walk(self,tree):
			for tree in tree.trees:
				for blob in tree.blobs: # files
					self.result.append(blob.path)
				self.walk(tree)
	repo = Repo(os.getcwd())
	repo.head.reference.commit = hash
	instance=git_files_list()
	instance.walk(repo.head.commit.tree)
	return instance.result

os.chdir("/Users/nordmenss/git/pg_test")

git_files=files("1440c5db76e9605d5bcd234dda56a0a5b7184a13")
for l in git_files:
	print l