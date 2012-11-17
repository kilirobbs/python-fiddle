from lxml import etree
from StringIO import StringIO


parser = etree.XMLParser(ns_clean=True,remove_blank_text=True)
xml = '<a xmlns="test"><b xmlns="test"/></a>'
tree   = etree.parse(StringIO(xml), parser)
print etree.tostring(tree.getroot())

