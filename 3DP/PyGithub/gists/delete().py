from github import Github

import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)
for gist in g.get_user().get_gists():
    print "\n\n"
    print "description=", gist.description
    print "id=", gist.id
    gist.delete()