from xml.dom import minidom
import urllib

url = "http://www.earthtools.org/sun/55.120010/33.233448/15/10/3/0"
xml = urllib.urlopen(url).read()

xmldoc = minidom.parseString(xml)

def tree(xml):
    class node(object):
        pass

    def rec(e):
        if len(e.childNodes) == 1 and (e.nodeType == e.TEXT_NODE or e.nodeType == e.ELEMENT_NODE):
            return e.childNodes[0].nodeValue
        else:
            self = node()
            for child in e.childNodes:
                if child.nodeType != child.TEXT_NODE:
                    print "child.nodeName=", child.nodeName
                    setattr(self, child.nodeName, rec(child))
            return self
    return rec(xml)

sun = tree(xmldoc).sun
print sun.day
