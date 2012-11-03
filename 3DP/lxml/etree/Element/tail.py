from lxml import etree
root = etree.Element("root", interesting="totally")
root.text="Text inside tag"
root.tail="text after tag"
print(etree.tostring(root, pretty_print=True))
# <root interesting="totally">Text inside tag</root>text after tag