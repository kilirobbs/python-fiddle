# -*- coding: utf-8 -*-
from envoy import run

try:
    r = run('error', timeout=2)
    print r.status_code
    print r.std_out
    print r.std_err
    print r.command
except Exception,e:
    print str(e)


print run('osascript -e "error"').status_code