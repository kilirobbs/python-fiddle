import os
import sys
import platform
from sys import version_info as v

print platform.system()

print v
print v.major
print v[0]
# sys.version_info(major=2, minor=7, micro=1, releaselevel='final', serial=0)

print v.major

print platform.python_version()
# 2.7.1

print platform.mac_ver()

print "python_version_tuple()=", platform.python_version_tuple()

print os.name