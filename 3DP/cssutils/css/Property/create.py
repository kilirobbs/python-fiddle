import cssutils

# http://packages.python.org/cssutils/docs/css.html#property

prop=cssutils.css.Property(name='background', value=u'white url(paper.png) scroll', priority=u'')
print prop
print prop.name, prop.cssText # background: white url(paper.png) scroll
print prop.propertyValue