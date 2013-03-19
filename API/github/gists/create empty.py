#!/usr/bin/env python
from json import dumps
from requests import post
from gitconfig import gitconfig

r = post('https://api.github.com/gists', 
    data=dumps({
        "description":"new empty",
        "public": True,
        "files" : dict()
    }),
    auth=(gitconfig.user.name, gitconfig.github.password)
)
print r.json