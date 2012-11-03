print "1,2,3".split(",")
# ['1', '2', '3']

print "1,2,3".split(",")[0:2]


key,value="key=value".split("=")
print key, value


filename="path/to/schema/schemaname/table/tablename"
print "parent=","/".join(filename.split("/")[0:-2])

print "tablename=",filename.split("/")[-2]

def path2cls(path):
	try:
		print path.split("/")[-2]
		return {
			'LANGUAGE'	: 'LANGUAGE'
		}[ path.split("/")[-2] ]
	except:
		raise ValueError("unknown class for '%s'" % path)

print path2cls("LANGUAGE/plpgsql")