#!/usr/bin/env python
from json import dumps
from requests import post
from gitconfig import gitconfig

empty=True
if not empty:
    r = post('https://api.github.com/gists', 
        data=dumps({
            "description":"desc",
            "public": True,
            "files": {
                "filename": {
                  "content": "String file contents"
                }
            }
        }),
        auth=(gitconfig.user.name, gitconfig.github.password)
    )
else:
    r = post('https://api.github.com/gists', 
        data=dumps({
            "description":"desc",
            "public": True,
            "files":{
                "filename.empty": {
                    "content": "I'm empty :( don't live me alove, %s" % gitconfig.user.name
                }
            }
        }),
        auth=(gitconfig.user.name, gitconfig.github.password)
    )
print r.json