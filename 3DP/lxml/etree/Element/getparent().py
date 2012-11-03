from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
root.tail="text after tag"
br = etree.SubElement(root, "br")

print(etree.tostring(root, pretty_print=True))
# <root>Text inside tag<br/></root>text after tag

print br.getparent()
# <Element root at 0x106d025f0>