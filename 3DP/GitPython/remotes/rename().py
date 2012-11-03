from git import *
repo = Repo("/Users/nordmenss/Library/Application Support/Sublime Text 2/Packages/AutoGit")

github = repo.remotes.github  # get by name
#origin = github.rename('origin')