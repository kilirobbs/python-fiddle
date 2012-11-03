from lxml import etree
from StringIO import StringIO


parser = etree.XMLParser(ns_clean=True,remove_blank_text=True)
xml = '<a xmlns="test"><b xmlns="test"/></a>'
tree   = etree.parse(StringIO(xml), parser)
print etree.tostring(tree.getroot())

# http://lxml.de/1.3/parsing.html

# Available boolean keyword arguments:
#	attribute_defaults - read the DTD (if referenced by the document) and add the default attributes from it
#	dtd_validation - validate while parsing (if a DTD was referenced)
#	load_dtd - load and parse the DTD while parsing (no validation is performed)
#	no_network - prevent network access when looking up external documents
#	ns_clean - try to clean up redundant namespace declarations
#	recover - try hard to parse through broken XML
#	remove_blank_text - discard blank text nodes between tags
#	remove_comments - discard comments
#	compact - use compact storage for short text content (on by default)