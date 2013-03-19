#!/usr/bin/env python
from ConfigParser import RawConfigParser
from os.path import expanduser

config = RawConfigParser()
print config.read(expanduser("~/.pypirc"))
print config.get('pypi', 'username')
try:
    print config.get('pypi', 'not_existing')
except:
    print "not_existing"