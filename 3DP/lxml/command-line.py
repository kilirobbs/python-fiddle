import sys
from lxml import etree
sys.argv.append("./sun.xml")
doc = etree.parse(sys.argv[1])
print doc.xpath("//latitude/text()")[0]