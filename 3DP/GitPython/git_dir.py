import os
from git import Repo
repo = Repo("/Users/nordmenss/git/pg_test/SCHEMA")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
print repo.git_dir

print os.path.dirname(repo.git_dir)