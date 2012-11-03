from datetime import datetime
import time

now = datetime.now()
print "now=", now
next_min = datetime(now.year, now.month, now.day, now.hour, now.minute + 1)
print "next_min=", next_min

today = datetime(now.year, now.month, now.day)
print "today=",today