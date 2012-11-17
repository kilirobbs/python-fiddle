from datetime import datetime

def date(text):
    return datetime.strptime(text,'%H:%M:%S').date()

print date("10:10:10")