import cssutils

# http://packages.python.org/cssutils/docs/css.html#propertyvalue

css = 'normal 1em/5 Arial, sans-serif, url(example.gif), func(1,2/*comm*/)'

for v in cssutils.css.PropertyValue(css):
	print v
	print "type=",v.type
	print v.__class__ # cssutils.css.value.Value, cssutils.css.value.DimensionValue, cssutils.css.value.CSSFunction
	if v.__class__==cssutils.css.value.URIValue:
		print "uri=",v.uri

	print ""

#for i, v in enumerate(pv):
	#print i, v