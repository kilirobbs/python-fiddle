import os
from os.path import expanduser
import plistlib
plist="~/Library/LaunchAgents/homebrew.mxcl.nginx.plist"
pl = plistlib.readPlist(os.path.expanduser(plist))
print pl

plistfile=expanduser("~/Library/Preferences/com.apple.iCal.plist")

pl = plistlib.readPlist(plistfile)