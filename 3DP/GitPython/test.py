#!/usr/bin/env python
from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
print repo.untracked_files