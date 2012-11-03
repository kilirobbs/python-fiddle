import requests
id = 3840699
token = "9c28da5f43b5342e33a9a6932d698feb5b15bca4"
params = dict(files=dict(filename="Default (OSX).sublime-keymap", content="test"))
url = 'https://api.github.com/gists/%s?access_token=%s' % (id, token)
url = 'https://api.github.com/gist/%s' % id
print url
r = requests.patch(url)
print r.text