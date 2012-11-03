from github import Github
import macos
g = Github(macos.user.gitconfig.user.name, macos.user.gitconfig.github.password)
i = 0
for e in g.get_user(macos.user.gitconfig.user.name).get_events():
    print ""
    print "repo=",e.type
    print "payload=",e.payload
    print "repo=",e.repo.__dict__
    print i, e.created_at, e.created_at.__class__, e.actor.login, e.actor.avatar_url
    print e.payload
    i += 1
    if i > 30:
        import sys
        sys.exit(1)
