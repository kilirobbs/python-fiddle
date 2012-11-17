from relaxml import xml
import requests as req
url='http:export.yandex.ru/weather-ng/forecasts/26686.xml'
content = req.get(url).text
print content
print xml(content)