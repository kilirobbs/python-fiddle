l=[1,2,3,4,5]

for i in xrange(0,len(l)):
    print l[i]


l1=[1,2,3,4,5]
l2=[1,2,3,4,5,6,7]

print "\nnew:"
for i in xrange(len(l1),len(l2)):
	print l2[i]

print "\nreverse:"
for i in xrange(len(l2),len(l1)):
	print l1[i]