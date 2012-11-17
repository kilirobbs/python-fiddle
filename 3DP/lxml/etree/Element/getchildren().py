from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
root.tail="text after tag"
br = etree.SubElement(root, "br")

print root.getchildren()