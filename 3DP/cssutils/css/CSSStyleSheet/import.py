import cssutils 
sheet = cssutils.parseString('@import url(http://pogoda.tut.by/css/by2/weather1.css);')

print sheet.__class__

print sheet.cssRules[0].styleSheet.variables.__dict__
