l=[3,2,1]
l.sort()
print l

def level(path):
	return (path.count("/")+1) / 2

l=["filename.oid","filename.sql","filename.references",\
"filename2.oid","filename2.sql","filename2.references"]
l.sort(key=lambda v: v.find(".sql")<0)
print "\n\nsort by .sql first:"
print l
