# -*- coding: utf-8 -*-
import os
import urllib
from requests import get
url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
r=get(url)
print r.encoding
print r.headers['Content-Type']
data=r.text
print data.__class__
data=data.encode('utf8')
data=urllib.urlopen(url).read()
print data.__class__
f=os.path.expanduser("~/Downloads/forecast.xml")
f = open(f, 'w')
f.write(data)
f.close()