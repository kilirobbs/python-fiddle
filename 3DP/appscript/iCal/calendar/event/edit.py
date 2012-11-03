from appscript import *
from datetime import datetime


uid = "792C9DB4-E3AD-4327-B6D4-94EEFB15182C"


events = app('iCal').calendars.events[its.uid == uid]()
for event in events:
    if event != []:
        event = event[0]
        s = event.start_date()
        end = event.end_date()
        print "start=", s
        print "end=", end
        print "start.hour=", s.hour
        new_s = datetime(s.year, s.month, s.day, s.hour + 1, s.minute)
        print "new_start=", new_s
        event.start_date.set(new_s)
        event.end_date.set(new_s)
        #event.end_date.set(end)