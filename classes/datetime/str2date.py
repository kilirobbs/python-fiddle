#!/usr/bin/env python
from datetime import date, datetime
from dateutil import tz
from dateutil.parser import parse

now = datetime.now()
s = now.strftime('%Y-%m-%d %H:%M')
print  datetime.strptime(s, '%Y-%m-%d %H:%M')


print datetime.strptime("07:53:16", '%H:%M:%S')
print datetime.strptime("2012-10-10 07:53:16"[:10], '%Y-%m-%d')

#print datetime.strptime("2012-11-31T11:52:09", '%Y-%m-%dT%H:%M:%S')

s = '2008-09-03T20:56:35.450686Z'
print parse(s).astimezone(tz.tzutc())

print parse("10:10:10") # time
# 2013-01-29 10:10:10
