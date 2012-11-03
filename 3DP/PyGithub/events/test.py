from github import Github, InputFileContent
import macos
import sys

user=macos.user.gitconfig.user.name
password=macos.user.gitconfig.github.password
g = Github(user, password)


# create_gist(public, files, description)
files = dict(filename1=InputFileContent("filename1 content"))
for i,e in enumerate(g.get_user(user).get_events()):
    print e.payload
    if i>=10:
        sys.exit(1)