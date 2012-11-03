from datetime import datetime, timedelta



now = datetime.now()
next=now + timedelta(hours=2)
diff=next-now
print diff, diff.__class__
print diff.days
print diff.seconds
print diff.microseconds

def today(timedelta):
	return timedelta.seconds/3600

def hours(timedelta):
	return timedelta.seconds/3600

print hours(diff)