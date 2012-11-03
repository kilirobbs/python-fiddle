from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
tree=repo.head.commit.tree

print "trees=",tree.trees

def rec(tree):
	for tree in tree.trees:
		print "tree=",tree.path
		#for entry in tree.traverse():
			#print "entry=",entry.path

		for blob in tree.blobs: # files
			print "blob.hexsha=",blob.hexsha
			#print "blob.name=",blob.name
			#print "blob.path=",blob.path
			#print "blob.abspath=",blob.abspath
			#print "blob.mime_type=",blob.mime_type
			#print "blob.mode=",blob.mode
			#print "blob.data_stream().read()=",blob.data_stream.read()
		rec(tree)

rec(tree)