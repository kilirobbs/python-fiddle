import timeit
s = """\
	try:
		str.__nonzero__
	except AttributeError:
		pass
	"""
t = timeit.Timer(stmt=s)
print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)