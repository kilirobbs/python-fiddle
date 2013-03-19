#!/usr/bin/env python
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

url="http://www.github.com/cancerhermit/repo"
print urlparse(url)