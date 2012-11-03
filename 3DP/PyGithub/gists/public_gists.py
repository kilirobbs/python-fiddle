from github import Github

import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)

print g.get_user().public_gists