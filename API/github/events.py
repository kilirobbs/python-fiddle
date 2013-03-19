#!/usr/bin/env python
from requests import get

r = get('https://api.github.com/events')
print r.json