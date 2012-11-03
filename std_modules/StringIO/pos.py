import StringIO

f = StringIO.StringIO("first line")
print f.pos
f.seek(len(f.read()))
print f.pos