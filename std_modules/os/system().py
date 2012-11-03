# -*- coding: utf-8 -*-
import sys, os
s=u'echo "Привет"'
s=s.encode(sys.getfilesystemencoding())
print s
os.system(s)