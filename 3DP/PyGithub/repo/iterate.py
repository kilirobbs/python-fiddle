from github import Github

import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)

for r in g.get_user().get_repos():
    print r.name, r.description