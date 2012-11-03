d1	= dict({"1":"value1","2":"value2"})
d2	= dict({"1":"value1"})

# http://code.activestate.com/recipes/59875-finding-the-intersection-of-two-dicts/
intersect_keys = filter(d1.has_key, d2.keys())

print intersect_keys