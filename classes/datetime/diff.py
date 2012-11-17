from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


now = datetime.now()
next=now + timedelta(hours=2)
diff=next-now
print diff, diff.__class__
print diff.days
print diff.seconds
print diff.microseconds

print "relativedelta"
diff = relativedelta(next, now)
print diff,diff.__class__
print diff.days 
print diff.hours # 8
print diff.minutes 