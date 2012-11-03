import __builtin__
builtin_types= [t
	for t in __builtin__.__dict__.itervalues()
	if isinstance(t, type)]

print "\n".join(map(str,builtin_types))

print "\n\ncreate"
for t in builtin_types:
	try:
		t()
	except Exception, e:
		print type(e)