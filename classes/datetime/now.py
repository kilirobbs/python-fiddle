from datetime import datetime
import time

now = datetime.now()
print now
# 2012-09-09 18:24:57.932319
print "str(now)[0:10]=", str(now)[0:10]
# 2012-10-15

print "str(now)[0:16]=", str(now)[0:16]

print "str(now)[11:16]=", str(now)[11:16]
# 2012-10-15

print "datetime=", str(now)[0:16]
# 2012-10-15

print str(datetime.now())[:19]
print time.timezone / (60 * 60)
print "datetime.datetime.utcnow()=", datetime.utcnow()

print now.tzinfo
