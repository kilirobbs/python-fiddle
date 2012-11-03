from git import *
repo = Repo("/Users/nordmenss/git/test")

print repo.remotes
for r in repo.remotes:
    print "name=", r.name, "url=", r.url

print repo.remotes[0].url