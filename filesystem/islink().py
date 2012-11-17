import os

link="/Users/nordmenss/Library/LaunchAgents/com.apple.every.min.plist"
print os.path.islink(link)
print open(link).read()

print os.path.realpath(link)