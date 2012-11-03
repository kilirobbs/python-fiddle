from lxml import etree
from StringIO import StringIO
import urllib


tree = etree.parse("../sun.xml") # parse file

# tree = etree.parse(urllib.urlopen("http://www.google.com/")) # parse string

# print(tree.docinfo.doctype)

print tree.getroot()