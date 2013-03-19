#!/usr/bin/env python
from os.path import expanduser
from markdown import markdown
print markdown("""
Install
-----------

""")
_in="README.md"
_out="README.html"
print open(_in).read()
open(_out,"w").write(markdown(open(_in).read()))