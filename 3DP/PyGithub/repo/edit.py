from github import Github
import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)

print g.get_user().get_repo("name")
g.get_user().get_repo("name").edit(description="new description")