from appscript import *
from datetime import datetime
calendars = app('iCal').calendars
for calendar in calendars.get():
    print calendar.properties()
