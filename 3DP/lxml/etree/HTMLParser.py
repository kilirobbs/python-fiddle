from lxml import etree
from StringIO import StringIO

broken_html = "<html><head><title>test<body><h1>page title</h3>"

parser = etree.HTMLParser()
tree   = etree.parse(StringIO(broken_html), parser)

print etree.tostring(tree.getroot(), pretty_print=True)