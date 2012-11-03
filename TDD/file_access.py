import cStringIO

tempfile = cStringIO.StringIO()
print tempfile.__class__
print open("/Users/nordmenss/.pgpass").__class__
def write(h):
    h.write("Mary had a little lamb.\n")

write(tempfile)

tempfile.seek(0)
result = tempfile.read()