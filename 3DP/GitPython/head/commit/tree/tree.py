from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
tree=repo.head.commit.tree

print "tree",tree
print "tree.type",tree.type
print "tree.size",tree.size
print "tree.hexsha",tree.hexsha
print "tree.path=[%s]" % tree.path # root tree has no path
print "tree.mode=",tree.mode