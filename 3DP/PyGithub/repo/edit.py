from github import Github
import macos
g = Github(macos.user.gitconfig.user.name, macos.user.gitconfig.github.password)

print g.get_user().get_repo("githubhook")
repo=g.get_user().get_repo("githubhook")
print repo.edit
repo.edit("new description")