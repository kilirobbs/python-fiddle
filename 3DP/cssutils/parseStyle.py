import cssutils

# http://packages.python.org/cssutils/docs/parse.html#parsestyle
css="color:red;"

sheet = cssutils.parseStyle(css)
print sheet.__class__
# <class 'cssutils.css.cssstyledeclaration.CSSStyleDeclaration'>

for property in sheet.getProperties(): 
	print property.name, "-->", property.value 


css="background: transparent url(http://img.tut.by/weather/bg_1/8.jpg) top left no-repeat;"

sheet = cssutils.parseStyle(css)

for property in sheet.getProperties(): 
	print property.name, "-->", property.value 
	if len(property.propertyValue)>1:
		for v in property.propertyValue:
			if v.type=="URI":
				print v.value