# -*- coding: utf-8 -*-
from appscript import *

for calendar in app('iCal').calendars():
    for todo in calendar.todos():
        todo.delete()
