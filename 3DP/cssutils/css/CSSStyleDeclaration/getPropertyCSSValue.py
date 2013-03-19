import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssutils.css.CSSStyleDeclaration.getPropertyCSSValue

style = cssutils.css.CSSStyleDeclaration(cssText='background: transparent url(http://img.tut.by/weather/bg_2/weather_b/008.jpg) top center no-repeat')
if "background" in style.keys():
	for property in style.getPropertyCSSValue("background"): #a list of Property objects set in this declaration.
		print property