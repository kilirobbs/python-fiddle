import cssutils

sheet=cssutils.parseUrl("http://pogoda.tut.by/css/by2/weather1.css")
print sheet.__class__
# <class 'cssutils.css.cssstylesheet.CSSStyleSheet'>

for rule in sheet:
	print rule