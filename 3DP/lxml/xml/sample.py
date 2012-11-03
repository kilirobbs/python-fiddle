# http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
import lxml.html
import lxml.etree

url = 'https://github.com/cancerhermit.atom'
#url = "http://www.greenbuttondata.org/data/15MinLP_15Days.xml"
lxml.etree.parse(url)