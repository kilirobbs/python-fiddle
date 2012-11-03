from git import *
repo = Repo("/Users/nordmenss/git/pg_test")

from git.objects.base import Object
# Implements an Object which may be Blobs, Trees, Commits and Tags
binsha=repo.head.commit.binsha
f=Object(repo, binsha)
print f.__class__