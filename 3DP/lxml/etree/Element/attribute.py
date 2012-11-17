from lxml import etree
root = etree.Element("root", interesting="totally")
root.text = "TEXT"
print(etree.tostring(root, pretty_print=True))
# <root interesting="totally">TEXT</root>

root.set("interesting", "somewhat")
print(root.get("interesting"))


print root.attrib
# {'interesting': 'somewhat'}