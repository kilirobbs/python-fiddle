from git import *
repo = Repo()

for r in repo.remotes:
    print "name=", r.name, "url=", r.url
    r.pull(repo.head.reference)

repo.remotes[0].pull(repo.head.reference)
