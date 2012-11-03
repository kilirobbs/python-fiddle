import StringIO

f = StringIO.StringIO("test")
print f.getvalue()
f.truncate(2)
print f.getvalue()
f.truncate(0)
print f.getvalue()