# -*- coding: utf-8 -*-
from appscript import *

for calendar in app('iCal').calendars():
    for todo in calendar.todos():
        #print todo.properties()
        print todo.uid()
        print todo.due_date()
        print todo.url()
        print todo.summary().encode("utf-8")
        print todo.priority()
        print "completion_date=",todo.completion_date()  # k.missing_value
        print "stamp_date=",todo.stamp_date()
        print todo.description()