from appscript import *


def today(event):
for calendar in app('iCal.app').calendars():
    for event in calendar.events():
        print ""
        print "uid=", event.uid()
        print "allday_event", event.allday_event()
        if event.description() != k.missing_value:
            print "event.description()=", event.description().encode("utf-8")

        print "summary=", event.summary().encode("utf-8")
        print "end_date", event.end_date()
        print "start_date", event.start_date()
        print "stamp_date", event.stamp_date()
        print "recurrence", event.recurrence()
        print "url", event.url()
        print "location", event.location()
        print "excluded_dates", event.excluded_dates()
