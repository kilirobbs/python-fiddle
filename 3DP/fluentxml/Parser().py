from fluentxml import Parser
import requests

url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
xml=requests.get(url).text
tree=Parser(xml)
print tree.root.fact