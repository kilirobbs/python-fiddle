from icalendar import Calendar, Event
import os

def process_event(filename):
    e = Event.from_ical(open(filename, 'rb').read())
    for component in e.walk():
        if component.name == "VTODO":
            print component.get('calendar')
            print component.__dict__
        if component.name == "VEVENT":
            pass
            #print component.subcomponents
            #print component.get('summary')
            #print "dtstart=", component.get('dtstart').dt
            #print "dtend=", component.get('dtend').dt
            #print "dtstamp=", component.get('dtstamp').dt

def rec(path):
    for parent, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if os.path.splitext(file)[1] == ".ics":
                filename = os.path.join(parent, file)
                process_event(filename)


rec("/Users/nordmenss/Library/Calendars/6DF648F6-D60E-4FD4-9B86-D2B4FBB936A7.caldav")
