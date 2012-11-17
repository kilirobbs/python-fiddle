# -*- coding: utf-8 -*-
import os
import codecs
from requests import get
f=os.path.expanduser("~/Downloads/forecast.xml")
url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
r=get(url)
print r.encoding
open(f, 'w').write(r.text.encode(r.encoding))
content=codecs.open(f,"r",r.encoding).read()
print content