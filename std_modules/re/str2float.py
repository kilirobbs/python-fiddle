# http://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string-in-python

import re
print re.findall("\d+.\d+", "Current Level: 13.4 db.")[0]