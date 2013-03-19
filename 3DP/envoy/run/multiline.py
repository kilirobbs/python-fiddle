#!/usr/bin/env python
from envoy import run

cmd="""/usr/local/bin/growlnotify -t "nosetests --with-xunit" -m "finished 00:00:00

~/git/python/"  -a "Terminal"
"""
r=run(cmd)
print r.std_out,r.std_err