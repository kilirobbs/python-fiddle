import sys
import os

for module in sys.modules:
    print module

l = sys.modules.keys()
l.sort()
print "sys.modules.keys()=", "\n".join(l)
