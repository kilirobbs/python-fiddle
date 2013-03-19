#!/usr/bin/env python
from git import *
repo = Repo("/Users/nordmenss/git/FIDDLE/bash-fiddle")

print repo.remotes
for r in repo.remotes:
    print "name=", r.name, "url=", r.url

print repo.remotes[0].url

from os.path import basename, splitext
for r in repo.remotes:
    if r.url.find("git@github.com")>=0:
        print splitext(basename(r.url))[0]