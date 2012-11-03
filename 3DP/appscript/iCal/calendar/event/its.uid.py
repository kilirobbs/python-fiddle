# -*- coding: utf-8 -*-
from appscript import *
from subprocess import PIPE, Popen, STDOUT

def fg(command):
    process = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
    r = process.communicate()
    if process.returncode != 0:
        raise SystemError(r[0])
    else:
        # remove line break
        return "\n".join(r[0].splitlines())

output = fg("/usr/local/bin/icalBuddy -nc -eed -uid eventsToday | sed -n '/uid:/p' | tr -d '[:blank:]uid:'")
#print output

def uid2event(uid):
    events = app('iCal').calendars.events[its.uid == uid]()
    for event in events:
        if event != []:
            return event[0]

def name2event(summary):
    events = app('iCal').calendars.events[its.summary == summary]()
    for event in events:
        if event != []:
            return event[0]

for l in output.splitlines():
    if len(l) == 36:  # uid, not error
        e = uid2event(l)
        #print e.uid()

print  name2event("test_event").uid()
