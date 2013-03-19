import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssstyledeclaration

style = cssutils.css.CSSStyleDeclaration(cssText='color: red;font-size:14px;')
print style.keys()
# ['color', 'font-size']