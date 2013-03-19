from requests import get
from gitconfig import gitconfig

r = get('https://api.github.com/users/%s/gists' % gitconfig.user.name, 
    auth=(gitconfig.user.name, gitconfig.github.password)
)
print "users/%s/gists" % gitconfig.user.name
for i,l in enumerate(r.json):
    print i,l["id"],l["git_pull_url"],l["html_url"],l