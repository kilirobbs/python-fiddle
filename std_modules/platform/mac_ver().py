import platform
# http://stackoverflow.com/questions/1777344/how-to-detect-mac-os-version-using-python
print platform.mac_ver()
v, _, _ = platform.mac_ver()
print float('.'.join(v.split('.')[:2]))