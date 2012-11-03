import re
import datetime
print re.sub("[^\d]", "_",str(datetime.datetime.now())[0:18])