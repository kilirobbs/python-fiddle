# http://packages.python.org/cssutils/docs/css.html#value

import cssutils

v=cssutils.css.Value("red")
print v.cssText
print v.type
print v.value