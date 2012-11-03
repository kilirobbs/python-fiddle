from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
print(etree.tostring(root, pretty_print=True))
# <root>Text inside tag</root>