import urllib
print urllib.urlopen("http://google.com/").read()

# POST 
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen(url, params)