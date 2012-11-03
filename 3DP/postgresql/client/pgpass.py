import os
from postgresql.utility.client.pgpass import *

filename = os.path.expanduser("~/.pgpass")
print parse(filename)
print lookup_password(parse(filename),("127.0.0.1","","",""))