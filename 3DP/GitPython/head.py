from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
headcommit = repo.head.commit
print "headcommit.__class__=", headcommit.__class__, headcommit


print repo.head.reference.name