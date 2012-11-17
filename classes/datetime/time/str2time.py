from datetime import datetime

def time(text):
    return datetime.strptime(text,'%H:%M').time()

print time("09:10")