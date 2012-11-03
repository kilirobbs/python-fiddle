from datetime import datetime
print "{:%d.%m.%Y}".format(datetime.now())
print datetime.now().__format__("%d.%m.%Y")