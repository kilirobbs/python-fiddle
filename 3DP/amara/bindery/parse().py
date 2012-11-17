from amara import bindery
import requests
url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
content=requests.get(url).text
tree = bindery.parse(content.encode("utf-8"))
#print tree.forecast
print tree.xml_qname