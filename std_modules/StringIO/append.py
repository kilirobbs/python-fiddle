import StringIO

f = StringIO.StringIO("first line")
def append(f,value):
	f.seek(len(f.read()))
	f.write("\n%s" % value)
append(f,"second line")
print f.getvalue()