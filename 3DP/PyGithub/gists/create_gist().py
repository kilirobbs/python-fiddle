from github import Github, InputFileContent
import sys
import macos
g = Github(macos.user.gitconfig.user.name, macos.user.gitconfig.github.password)


# create_gist(public, files, description)
files = dict(filename1=InputFileContent("filename1 content"))
gist=g.get_user().create_gist(True, files, "description")
print gist.id, gist.git_pull_url