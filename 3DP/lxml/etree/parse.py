from lxml import etree
from StringIO import StringIO
import urllib


tree = etree.parse("../sun.xml") # parse file
print tree.__class__
# <type 'lxml.etree._ElementTree'>
print tree.getroot().__class__
# <type 'lxml.etree._Element'>

print tree.getroot().tag