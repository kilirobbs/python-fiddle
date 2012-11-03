class classname():
    def __init__(self, name=None, order=None):
        self.name = name
        self.order = order

l = []
l.append(classname("order", 3))
l.append(classname("first name", 2))
l.append(classname("id", 1))

print "\noriginal:"
for i in l:
    print i.order, i.name

print "\nsorted by name:"
for i in sorted(l, key=lambda v: v.name):
    print i.order, i.name

# http://stygianvision.net/updates/python-sort-list-object-dictionary-multiple-key/
print "\ntwo keys sort:"
for i in sorted(l, key=lambda k: (k.order, k.name)):
    print i.order, i.name
