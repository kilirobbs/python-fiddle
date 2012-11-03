from lxml import etree
root = etree.Element("root")
root.text="Text inside tag"
root.tail="text after tag"
print(etree.tostring(root, pretty_print=True))

build_text_list = etree.XPath("//text()") # lxml.etree only!
stringify = etree.XPath("string()")

texts = build_text_list(root)
print texts
# ['Text inside tag', 'text after tag']

print stringify(root)
# Text inside tag

print texts[0].is_text,texts[1].is_text
# True False