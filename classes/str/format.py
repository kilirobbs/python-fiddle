print "%s.%s" % ("schema","table")

# named parameters
print '%(language)s has %(#)03d quote types.' % {'language': "Python", "#": 2}

print '''line {0}
line {1}
line {2}'''.format(1,2,3)


name="name"
s="%(name)s" % \
{
	"name" : "\nname (%s)" % name if name else ""
}
print s