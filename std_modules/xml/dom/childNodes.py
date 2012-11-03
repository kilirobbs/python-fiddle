from xml.dom import minidom
import urllib

url = "http://www.earthtools.org/sun/55.120010/33.233448/15/10/3/0"
xml = urllib.urlopen(url).read()


xmldoc = minidom.parseString(xml)
for child in xmldoc.childNodes:
    print "child.nodeName=", child.nodeName
    for subchild in child.childNodes:
        print ""
        print "subchild.nodeName=", subchild.nodeName
        print "subchild.nodeType=", subchild.nodeType
        print "child.childNodes=", len(subchild.childNodes)
        if len(subchild.childNodes) == 1:
            print subchild.childNodes[0].nodeType
            print subchild.childNodes[0].TEXT_NODE