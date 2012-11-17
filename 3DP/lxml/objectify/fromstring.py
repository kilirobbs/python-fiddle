# -*- coding: utf-8 -*-
from lxml import objectify
from requests import get

url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
xml=get(url).text
root=objectify.fromstring(xml.encode("utf-8"))
print(isinstance(root, objectify.ObjectifiedElement))

print root.text
print root.attrib.__class__,root.attrib
# lxml.etree._Attrib, {...}
print "hasattr",hasattr(root,"fact")
print float(root.fact.humidity)

print len(root.day)
for day in root.day:
    #print day.tag
    for p in day.day_part:
        print hasattr(p,"temperature")
        print hasattr(p,"temperature-data")
        print p["temperature-data"].avg