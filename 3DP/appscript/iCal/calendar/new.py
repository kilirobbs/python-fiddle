# -*- coding: utf-8 -*-
from appscript import app,k

new = app('iCal').calendars.end.make(new=k.calendar)
print new.uid()