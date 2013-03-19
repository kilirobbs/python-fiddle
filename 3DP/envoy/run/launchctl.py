#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists
from envoy import run

plist="/Users/nordmenss/Library/LaunchAgents/com.agent.проверка интернета.plist"#.replace(" ","\\ ")
print exists(plist)
#cmd="launchctl unload \"%s\"" % plist

#cmd.decode("utf-8")
#r=run(str(cmd))
#print r,r.status_code#
#print r.std_out,r.std_err


from subprocess import PIPE, Popen
process = Popen(["launchctl","unload","-w",
    plist
    #plist.replace(" ","\\ ")
], 
    stdout=PIPE, 
    stderr=PIPE
)
print plist
r=process.communicate()
print process.returncode,r