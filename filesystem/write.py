# -*- coding: utf-8 -*-
import os

namelist=["line1","line2"]

f = open('test.txt', 'w') # write
f.writelines(namelist)
for name in namelist:
    f.write(name)
f.close()

#open('test.txt', 'w').write(content) # one liner

f = open('test.txt', 'r+') # read & write
f.writelines(namelist)
f.close()

filename="not_existing_path/filename.sql"

if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))


from requests import get
url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
content=get(url).text
f=os.path.expanduser("~/Downloads/forecast.xml")

print "write utf-8"
#open(f,"w").write(content)
open(f,"w").write(str(content).encode("utf-8"))
