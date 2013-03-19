from github import Github
from gitconfig import gitconfig
g = Github(gitconfig.user.name, gitconfig.github.password)
i = 0
for e in g.get_user(gitconfig.user.name).get_events():
    print ""
    print e.__dict__
    print "repo=",e.type
    print "public=",e.public
    print "payload=",e.payload
    print "org=",e.org
    print "org=",e.org
    print "created_at=",e.created_at
    print "repo=",e.repo
    print "repo=",e.repo.__dict__
    print e.actor.login, e.actor.avatar_url
    print e.payload
    i += 1
    if i > 30:
        import sys
        sys.exit(1)
