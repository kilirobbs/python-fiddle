#!/usr/bin/env python
from requests import get
from gitconfig import gitconfig

url="https://api.github.com/events"
r = get(url,
    auth=(gitconfig.user.name,gitconfig.github.password)
)
print r

r = get(url,
    auth=("name","password")
)
print r,r.status_code

r = get(url,
    auth=(None,None)
)
print r,r.status_code

