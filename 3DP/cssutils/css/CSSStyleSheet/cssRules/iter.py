import cssutils
sheet = cssutils.css.CSSStyleSheet()
sheet.cssText = '@charset "ascii";a { color: green }'
for rule in sheet:
	print rule