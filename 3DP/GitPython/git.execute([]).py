from git import *
import os, os.path
g = Git("/Users/nordmenss/git/pg_test")
result = g.execute(["git", "commit", "-m", "'message'"])
print result