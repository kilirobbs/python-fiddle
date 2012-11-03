

# http://stackoverflow.com/questions/869885/loop-backwards-using-indices-in-python
for i in xrange(1, 10):
    print i
# 1-9

for i in range(10, -1, -1):
    print i,

print "\n\nfor i in reversed(xrange(10)):"
for i in reversed(xrange(10)):
    print i,

print "\n\nfor i in reversed(xrange(10)):"
for i in reversed(xrange(10)):
    print i
    if i < 5:
        break

for i, item in enumerate(["var1", "var2", "var3"]):
    print i, item
