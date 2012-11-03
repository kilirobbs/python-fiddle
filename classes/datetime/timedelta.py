from datetime import datetime, timedelta

now = datetime.now()
print now
print now + timedelta(1)  # next day
# next hour
print now + timedelta(weeks=0, days=0, hours=1, minutes=0, seconds=0)
# half hour back
print now+timedelta(weeks=0,days=0,hours=0,minutes=-30,seconds=0)