import cssutils
sheet = cssutils.parseString('@import url(weather.css); body { color: red }')
print sheet.cssText