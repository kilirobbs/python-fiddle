#!/usr/bin/env python
from requests import get
from gitconfig import gitconfig

r = get('https://api.github.com/gists', 
    auth=(gitconfig.user.name, gitconfig.github.password)
)
print r.json