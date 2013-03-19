import cssutils

# http://packages.python.org/cssutils/docs/parse.html#parsestring
css="color:red;"
sheet = cssutils.parseStyle(css)
print sheet.__class__
# <class 'cssutils.css.cssstyledeclaration.CSSStyleDeclaration'>