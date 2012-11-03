from lxml import etree
from StringIO import StringIO
import urllib


tree = etree.parse("../sun.xml") # parse file

print tree.getroot()