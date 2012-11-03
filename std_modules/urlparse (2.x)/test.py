from urlparse import urlparse

url = 'http://www.cwi.nl:80/%7Eguido/Python.html?param1=value1'
print urlparse(url)
print "netloc=", urlparse(url).netloc
print "path=",urlparse(url).path