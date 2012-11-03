import json
l = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print l.__class__
print l
print "\nitems:"
for i in l:
    print i.__class__, i
