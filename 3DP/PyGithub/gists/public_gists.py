from github import Github
from gitconfig import gitconfig

g = Github(gitconfig.user.name, gitconfig.github.password)
print g.get_user().public_gists