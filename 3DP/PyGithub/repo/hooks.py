from github import Github

import macos
g = Github(macos.user.gitconfig.user.name, macos.user.gitconfig.github.password)

r=g.get_user().get_repo("setup-py")
for hook in r.get_hooks():
    print '%s:%s (%s)' % (r.name, hook.id, hook.name)