from github import Github

import macos
g = Github(macos.user.gitconfig.user.name, macos.user.gitconfig.github.password)
for gist in g.get_user().get_gists():
    print "\n\n"
    print gist._requester.__dict__
    print "description=", gist.description
    print "id=", gist.id
    print "user=", gist.user
    print "forks=", gist.forks
    print "files=", gist.files
    print "files.keys()=", gist.files.keys()
    for filename, file in gist.files.iteritems():
        print "\nfilename=", filename
        print "language=", file.language
        print "raw_url=", file.raw_url
        print "size=", file.size
        print "content=", file.content
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