# -*- coding: utf-8 -*-
from lxml import objectify
from requests import get

url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
xml=get(url).text
root=objectify.fromstring(xml.encode("utf-8"))


print "\n".join([l.tag for l in root.fact.iterchildren()])