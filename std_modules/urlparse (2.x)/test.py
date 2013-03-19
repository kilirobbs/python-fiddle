from urlparse import urlparse

url = 'http://www.cwi.nl:80/%7Eguido/Python.html?param1=value1'
print urlparse(url)
print "netloc=", urlparse(url).netloc
print "path=",urlparse(url).path

giturl="git@github.com:cancerhermit/PyGithubMarkdown2HTML.git"
if not urlparse(giturl).scheme:
   giturl = "http://"+giturl
print "git@"+urlparse(giturl).hostname