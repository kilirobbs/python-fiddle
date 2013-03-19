#!/usr/bin/env python
from appscript import app

Safari = app('Safari')
if Safari.windows.count():
    for i,window in enumerate(Safari.windows()):
        print window.tabs()
        tabs=window.tabs()
        print tabs
        if tabs:
            for j,tab in enumerate(tabs):
                print j,tab.properties()
else:
    print "0 windows"
