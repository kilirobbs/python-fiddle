import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssutils.css.CSSStyleDeclaration.setProperty

style = cssutils.css.CSSStyleDeclaration(cssText='color: red;font-size:14px;')
style.setProperty("color",value="green")
print style