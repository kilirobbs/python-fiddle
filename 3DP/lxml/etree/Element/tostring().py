from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
root.tail="text after tag"
print(etree.tostring(root, pretty_print=True))
# <root>Text inside tag</root>text after tag

print "method=html:", etree.tostring(root, method="html")
# <root>Text inside tag</root>text after tag

print "method=text:", etree.tostring(root, method="text")
# Text inside tagtext after tag

print "method=xml:",etree.tostring(root, method="xml")
# <root>Text inside tag</root>text after tag

print etree.tostring(root, with_tail=False)
# <root>Text inside tag</root>

print etree.tostring(root, xml_declaration=True)


print etree.tostring(root, encoding='iso-8859-1')
