import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssutils.css.CSSStyleDeclaration.getPropertyPriority

style = cssutils.css.CSSStyleDeclaration(cssText='background: transparent url(http://img.tut.by/weather/bg_2/weather_b/008.jpg) top center no-repeat')
print style.getProperty("background").value
print style.background