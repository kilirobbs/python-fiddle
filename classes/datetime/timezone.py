from time import gmtime, strftime
print strftime("%z", gmtime())
print int(strftime("%z", gmtime())) / 100

import time
print time.timezone
print -time.timezone / 3600
print int(strftime("%z", gmtime())) / 100