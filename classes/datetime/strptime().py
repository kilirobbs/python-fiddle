#!/usr/bin/env python
from datetime import date, datetime
from time import strptime

now = datetime.now()
s = now.strftime('%Y-%m-%d %H:%M')
t = strptime(s, '%Y-%m-%d %H:%M')
print t.tm_year

print now.strftime('%H:%M')