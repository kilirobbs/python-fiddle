from github import Github, InputFileContent

import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)
for gist in g.get_user().get_gists():
    print ""
    print gist.id, gist.description
    print g.get_gist(gist.id)
    # def edit(self, description=GithubObject.NotSet, files=GithubObject.NotSet):
    print g.get_gist(gist.id).edit(description="description")