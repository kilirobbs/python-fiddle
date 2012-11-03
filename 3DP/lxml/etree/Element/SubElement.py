# http://lxml.de/tutorial.html

from lxml import etree
html = etree.Element("html")
body = etree.SubElement(html, "body")

br = etree.SubElement(body, "br")

print(etree.tostring(html, pretty_print=True))