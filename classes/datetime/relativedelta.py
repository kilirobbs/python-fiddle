#!/usr/bin/env python
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


now = datetime.now()
next=now - timedelta(hours=2,minutes=30)
diff = relativedelta(next, now)
print diff,diff.__class__
print diff.hours
print diff.minutes
print diff.seconds
