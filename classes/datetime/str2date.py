from datetime import date, datetime

now = datetime.now()
s = now.strftime('%Y-%m-%d %H:%M')
print  datetime.strptime(s, '%Y-%m-%d %H:%M')


print datetime.strptime("07:53:16", '%H:%M:%S')
print datetime.strptime("2012-10-10 07:53:16"[:10], '%Y-%m-%d')

print datetime.strptime("2012-11-06T11:52:09", '%Y-%d-%mT%H:%M:%S')