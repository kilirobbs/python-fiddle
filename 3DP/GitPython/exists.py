from git import Repo

path = "/Users/nordmenss/git/seowin"
try:
    repo = Repo(path)
except:
    print "not git repository"
