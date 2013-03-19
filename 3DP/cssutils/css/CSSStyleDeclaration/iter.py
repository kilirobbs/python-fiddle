import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssutils.css.CSSStyleDeclaration.getPropertyPriority

style = cssutils.css.CSSStyleDeclaration(cssText='background: transparent url(http://img.tut.by/weather/bg_2/weather_b/008.jpg) top center no-repeat')
for i,prop in enumerate(style):
	print prop
	print "%s) name=%s, value=%s" % (str(i+1),prop.name,prop.value)