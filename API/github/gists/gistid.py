#!/usr/bin/env python
from os.path import expanduser
from urlparse import urlparse
from git import Repo

def gistid(repo):
    for r in repo.remotes:
        if r.url.find("gist.github.com")>0:
            return urlparse(r.url).path.split("/")[1].split(".")[0]

print gistid(Repo(expanduser("~/git/GISTS/4039460")))