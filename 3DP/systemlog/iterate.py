#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import exists, expanduser
from pickle import dump, load
from re import findall, sub
from growlnotify import growlnotify
from systemlog import items

f = expanduser("~/.launchd.syslog")
if exists(f):
    checked = load(open(f))
else:
    checked = datetime.now()

for i in items():
    if i.process.find("com.apple.launchd.peruser") >= 0:
        if i.datetime > checked:
            subprocess = findall("\(.*\)", i.process)[0][1:-1]
            label = sub("[\[\d\]]", "", subprocess)
            print "\nstr=", i.str
            print "label=", label
            print i.datetime.strftime('%H:%M'), i.message

#dump(datetime.now(), open(f, "w"))
