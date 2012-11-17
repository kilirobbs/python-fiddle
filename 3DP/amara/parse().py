import amara
import requests
url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
content=requests.get(url).text
doc = amara.parse(content)