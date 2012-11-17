from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
root.tail="text after tag"
br = etree.SubElement(root, "br")

find = etree.XPath("//br")
print(find(root)[0].tag)