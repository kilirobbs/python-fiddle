from github import Github
from gitconfig import gitconfig

g = Github(gitconfig.user.name, gitconfig.github.password)
for gist in g.get_user().get_gists():
    print "\n\n"
    print "is_starred=",gist.is_starred()
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
        try:
            print "content=", file.content
        except:
            pass
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