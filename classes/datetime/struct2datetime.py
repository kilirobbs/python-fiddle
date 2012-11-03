# http://stackoverflow.com/questions/1697815/how-do-you-convert-a-python-time-struct-time-object-into-a-datetime-object
import time
from time import mktime
from datetime import datetime
struct = time.localtime()
dt = datetime.fromtimestamp(mktime(struct))
print dt