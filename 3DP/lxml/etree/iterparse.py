from lxml import etree
from StringIO import StringIO

some_file_like = StringIO("<root><a>data</a></root>")

for event, element in etree.iterparse(some_file_like):
	print("%s, %4s, %s" % (event, element.tag, element.text))


for event, element in etree.iterparse(some_file_like,events=("start", "end")):
	print("%5s, %4s, %s" % (event, element.tag, element.text))


for event, element in etree.iterparse(some_file_like):
	if element.tag == 'b':
		print(element.text)
	elif element.tag == 'a':
		print("** cleaning up the subtree")
		element.clear()