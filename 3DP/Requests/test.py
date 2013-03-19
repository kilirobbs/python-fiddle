#!/usr/bin/env python
from requests import get

url="https://gist.github.com/raw/4497462/connection%20check.py"
r = get(url)
print r.status_code # 200
print r.text
print r.json