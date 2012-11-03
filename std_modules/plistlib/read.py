import os
import plistlib
plist="~/Library/LaunchAgents/homebrew.mxcl.nginx.plist"
pl = plistlib.readPlist(os.path.expanduser(plist))
print pl