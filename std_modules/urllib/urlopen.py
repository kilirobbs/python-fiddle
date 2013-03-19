#!/usr/bin/env python
import sys
import urllib

def get(url):
    if sys.version_info.major==2:
        urllib.urlopen(url).read()
    else:
        urllib.request.urlopen().read()

get("http://google.com/")

