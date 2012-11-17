from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
br = etree.SubElement(root, "br")

print root.xpath("br")


# http://stackoverflow.com/questions/9233092/using-lxml-and-path-to-parse-xml-but-get-empty-list-if-it-has-xmlns-declaration?rq=1
# http://lxml.de/xpathxslt.html
url="http://export.yandex.ru/weather-ng/forecasts/26686.xml"
tree=etree.parse(url)
print tree.getroot().xpath("uptime")
# [] already if invalid xml
yesterday=tree.getroot().xpath("//*[local-name()='yesterday']")[0]
print "yesterday",yesterday
print ""
print "uptime in root:", int(yesterday.xpath("count(//*[local-name() = 'uptime'])"))
for r in yesterday.xpath("//*[local-name()='uptime']"):
    print r.text
print ""
print "uptime in this element:", int(yesterday.xpath("count(*[local-name() = 'uptime'])"))
for r in yesterday.xpath("*[local-name()='uptime']"):
    print r.text
ns=dict(a="http://weather.yandex.ru/forecast")
print tree.getroot().xpath("//a:uptime",namespaces=ns)
print yesterday.xpath("a:uptime/text()",namespaces=ns)