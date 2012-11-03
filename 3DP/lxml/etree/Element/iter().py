from lxml import etree
root = etree.Element("root")
etree.SubElement(root, "child").text = "Child 1"
etree.SubElement(root, "child").text = "Child 2"
etree.SubElement(root, "another").text = "Child 3"
root.append(etree.Entity("#234"))
root.append(etree.Comment("some comment"))


# http://lxml.de/tutorial.html

print(etree.tostring(root, pretty_print=True))

print ""
print "all elements:"
for element in root.iter():
	print("%s - %s" % (element.tag, element.text))

print ""
print "child only:"
for element in root.iter("child"):
	print("%s - %s" % (element.tag, element.text))


print ""
print "etree.Element only:"
for element in root.iter(tag=etree.Element):
	print("%s - %s" % (element.tag, element.text))