import StringIO

output = StringIO.StringIO("test")
print output.getvalue()
output.write('First line.\n')
print output.getvalue()
output.close()