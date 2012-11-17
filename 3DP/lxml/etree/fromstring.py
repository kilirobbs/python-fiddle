from lxml import etree

xml = '<a xmlns="test"><b xmlns="test"/></a>'

root = etree.fromstring(xml, base_url="http://where.it/is/from.xml")
print root, root.__class__