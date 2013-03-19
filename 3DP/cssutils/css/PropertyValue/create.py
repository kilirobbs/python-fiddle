import cssutils

# http://packages.python.org/cssutils/docs/css.html#propertyvalue

css = 'normal 1em/5 Arial, sans-serif, url(example.gif), func(1,2/*comm*/)'
pv = cssutils.css.PropertyValue(css)
print pv.cssText

for i, v in enumerate(pv):
	print i, v