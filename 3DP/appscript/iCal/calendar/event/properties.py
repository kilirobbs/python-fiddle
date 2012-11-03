from appscript import *

for calendar in app('iCal.app').calendars():
    for event in calendar.events():
        print event.properties()