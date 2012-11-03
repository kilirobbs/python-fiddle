import os
import StringIO
import cStringIO
print open(os.path.expanduser("~/.pgpass")).__class__
print cStringIO.StringIO().__class__
print StringIO.StringIO().__class__