import cssutils

sheet=cssutils.parseUrl("http://pogoda.tut.by/css/by2/weather1.css")
print sheet.__class__
# <class 'cssutils.css.cssstylesheet.CSSStyleSheet'>

for rule in sheet:
	if  rule.__class__==cssutils.css.cssstylerule.CSSStyleRule:
		for selector in rule.selectorList:
			if selector.selectorText==".w_n_8":
				if "background" in rule.style.keys():
					for property in rule.style.getPropertyCSSValue("background"): #a list of Property objects set in this declaration.
						if property.__class__==cssutils.css.value.URIValue:
							print property.uri