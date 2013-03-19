import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssutils.css.CSSRule.cssText
css="color:red;"

sheet = cssutils.parseStyle(css)
print sheet.__class__

sheet.cssRules[0].cssText