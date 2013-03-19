from requests import get
from gitconfig import gitconfig


r = get('https://api.github.com/gists/public', 
    auth=(gitconfig.user.name, gitconfig.github.password)
)
print "gists/public (all user)"
for i,l in enumerate(r.json):
    print i,l