from datetime import datetime
from os import environ
from time import gmtime, strftime
from pytz import timezone

print strftime("%z", gmtime())
print int(strftime("%z", gmtime())) / 100

import time
print time.timezone
print -time.timezone / 3600
print int(strftime("%z", gmtime())) / 100

environ['TZ'] = 'Europe/Moscow' # 'Europe/London'
print datetime.now()

environ['TZ'] = 'Europe/London'
print datetime.now().replace(tzinfo=timezone('UTC'))