#!/usr/bin/env python
from tempfile import gettempdir
from tempfile import mkstemp
# http://docs.python.org/library/tempfile.html#tempfile.mkstemp

print gettempdir()
# /var/folders/9d/l44q9nhx6_b93pny23s9l0ch0000gn/T
print mkstemp()
# (3, '/var/folders/9d/l44q9nhx6_b93pny23s9l0ch0000gn/T/tmpAZpLul')
print mkstemp()[1]