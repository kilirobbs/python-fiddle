from my_xml import parse
import requests

url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
xml=requests.get(url).text
tree=parse(xml)
print tree