#!/usr/bin/env python
from fluentxml import Parser
content=open('nosetests.xml').read()
print Parser
xml = Parser(content)
print xml
print "root",xml.root
print "root",xml.root.testcase # list
print "root",xml.root._children
for c in xml.root._children:
    print "c",c,c.__class__
