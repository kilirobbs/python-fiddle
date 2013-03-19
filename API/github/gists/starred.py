from requests import get
from gitconfig import gitconfig

r = get('https://api.github.com/gists/starred', 
    auth=(gitconfig.user.name, gitconfig.github.password)
)
print "gists/starred (my)"
for i,l in enumerate(r.json):
    print i,l