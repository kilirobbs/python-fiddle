from time import gmtime, strftime
from datetime import datetime

print strftime("%H:%M:%S", gmtime())
print strftime("%H:%M", gmtime())

t = strftime("%H:%M:%S", gmtime())
print t.tm_hour
print str(datetime.time(datetime.now()))[0:5]