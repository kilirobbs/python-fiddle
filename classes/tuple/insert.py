# http://stackoverflow.com/questions/2309329/inserting-an-item-in-a-tuple

a = ('Product', '500.00', '1200.00')
a = list(a)
a.insert(2, 'foobar')
a = tuple(a)
print a