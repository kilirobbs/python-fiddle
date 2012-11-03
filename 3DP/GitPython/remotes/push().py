from git import *
repo = Repo("/Users/nordmenss/Library/Application Support/Sublime Text 2/Packages/AutoGit")

print repo.remotes
for r in repo.remotes:
    print "name=", r.name, "url=", r.url
    r.push(repo.head.reference)

print ""
github = repo.remotes.github  # get by name
#origin = github.rename('origin')
#origin.push()