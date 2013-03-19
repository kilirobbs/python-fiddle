from urlparse import urlparse


giturl="git@github.com:cancerhermit/PyGithubMarkdown2HTML.git"
if not urlparse(giturl).scheme:
   giturl = "http://"+giturl
print "git@"+urlparse(giturl).hostname


giturl="https://gist.github.com/4379058.git"
netloc=urlparse(giturl).netloc
path=urlparse(giturl).path
print "netloc=",netloc
print "path=",path
if netloc.find("github.com")>=0:
    if giturl.find("https://")>=0:
        print giturl.replace("https://","git@")