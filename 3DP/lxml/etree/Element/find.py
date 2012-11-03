from lxml import etree

root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")

print(root.find("b"))

print(root.find("a").tag)
# a

print(root.find(".//b").tag)
# b

[ b.tag for b in root.iterfind(".//b") ]
# ['b', 'b']

print(root.findall(".//a[@x]")[0].tag)

# a
print(root.findall(".//a[@y]"))