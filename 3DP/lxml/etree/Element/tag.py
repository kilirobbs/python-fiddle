from lxml import etree
root = etree.Element("root")

print root.tag


def tag(elem):
    return elem.tag.rsplit('}', 1)[-1]