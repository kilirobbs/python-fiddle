# -*- coding: utf-8 -*-
# http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
import lxml.etree

url = 'http://export.yandex.ru/weather-ng/forecasts/26686.xml'
tree=lxml.etree.parse(url)

for r in tree.getroot():
    print r
#print tree.getroot().xpath("fact")
#print(lxml.etree.tostring(tree, pretty_print=True))