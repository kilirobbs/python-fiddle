from lxml import etree
root = etree.Element("root", interesting="totally")
print(etree.tostring(root, pretty_print=True))