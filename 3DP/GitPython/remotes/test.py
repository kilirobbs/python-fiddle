#!/usr/bin/env python
from git import Repo
d="/Users/nordmenss/git/GISTS/chrome toggle border css"
repo = Repo(d)

for r in repo.remotes:
    r.pull(repo.head.reference,"--rebase")