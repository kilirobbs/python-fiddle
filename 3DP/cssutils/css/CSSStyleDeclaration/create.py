import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssstyledeclaration

style = cssutils.css.CSSStyleDeclaration(cssText='color: red;font-size:14px;')
print style.__class__
# <class 'cssutils.css.cssstyledeclaration.CSSStyleDeclaration'>

print  cssutils.parseStyle("color:red;").__class__
# <class 'cssutils.css.cssstyledeclaration.CSSStyleDeclaration'>

style.color = 'green'
print style.color

del style.color
print style.color