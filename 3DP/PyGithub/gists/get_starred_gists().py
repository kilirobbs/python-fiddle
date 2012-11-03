from github import Github

import macos
g = Github(macos.gitconfig.user.name, macos.gitconfig.github.password)

for gist in g.get_user().get_starred_gists():
    print ""
    print "description=", gist.description
    print "id=", gist.id
    print "user=", gist.user
    print "forks=", gist.forks
    print "files=", gist.files
    print "public=", gist.public
    print "created_at=", gist.created_at
    print "updated_at=", gist.updated_at
    print "html_url=", gist.html_url
    print "created_at=", gist.created_at
    print "url=", gist.url
    print "fork_of=", gist.fork_of
    print "git_pull_url=", gist.git_pull_url
    print "git_push_url=", gist.git_push_url
    print "comments=", gist.comments