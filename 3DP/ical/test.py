# -*- coding: utf-8 -*-
from ical import ical

for c in ical.calendars:
    try:
        print c
    except:
        pass