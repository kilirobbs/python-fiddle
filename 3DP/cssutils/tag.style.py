import cssutils

# tag='<a href="url" style="color:red">inner html</a>'
css="color:red;"

sheet = cssutils.parseStyle(css)

for property in sheet.getProperties(): 
	print property.name, "-->", property.value 