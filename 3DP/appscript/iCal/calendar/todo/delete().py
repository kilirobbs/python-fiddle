# -*- coding: utf-8 -*-
from appscript import *

for calendar in app('iCal').calendars():
    for todo in calendar.todos():
        todo.delete()

uid="EC714096-78BE-4B09-85AC-832C71D283A5"
app('iCal').calendars.todos[its.uid==uid].delete()
