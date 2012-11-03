# http://stackoverflow.com/questions/9334762/how-to-find-element-attribute-using-lxml

rating = node.xpath('//t:rating', namespaces = {'t':'http://example/namespace'})
print rating[0].attrib['system']