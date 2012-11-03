import os
import sys
import platform
print sys.version_info
# sys.version_info(major=2, minor=7, micro=1, releaselevel='final', serial=0)

print sys.version_info.major

print platform.python_version()
# 2.7.1

print "python_version_tuple()=", platform.python_version_tuple()

print os.name