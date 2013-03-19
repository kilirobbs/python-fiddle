import os
from os.path import expanduser
import plistlib
plist="~/git/LaunchAgents/com.apple.every.min.plist"
pl = plistlib.readPlist(expanduser(plist))
print pl