#!/usr/bin/env python
from requests import get

r = get('https://api.github.com/repos/%s/%s/events' % \
        ("cancerhermit","Sublime.alfredextension")
    )
for e in r.json:
    print len(e.keys())
    print e