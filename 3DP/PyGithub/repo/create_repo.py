from github import Github

import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)
#g.get_user().create_repo(name, description, homepage, private, has_issues)