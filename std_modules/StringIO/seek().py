import StringIO

f = StringIO.StringIO("first line")
f.seek(len(f.read()))
print f.pos