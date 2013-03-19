import cssutils

# http://packages.python.org/cssutils/docs/css.html#cssstylerule

rule=cssutils.css.CSSStyleRule(".class", "color:red")
print rule
# <cssutils.css.CSSStyleRule object selectorText=u'.class' style=u'color: red' _namespaces={} at 0x106ef1ad0>
print rule.cssText
print rule.style
print "color:",rule.style.color


