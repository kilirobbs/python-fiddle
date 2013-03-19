#!/usr/bin/env python
from os.path import expanduser
from git.config import GitConfigParser

# stolen from gitpython/repo/base.py
f=expanduser("~/.gitconfig")
files = [f]
config = GitConfigParser(f, read_only=False)
print config.get("user", "name")
#print config.get("notexisting", "name")
# ConfigParser.NoSectionError: No section: 'notexisting'

config.set("key", "value")