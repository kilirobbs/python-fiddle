#!/usr/bin/env python
from appscript import app

safari = app('Safari')
if safari.windows.count():
    for i,w in enumerate(safari.windows()):
        print i,w.properties()
        print w.__dict__
        print w.AS_appdata.__dict__
        print w.AS_aemreference
else:
    print "0 windows"
