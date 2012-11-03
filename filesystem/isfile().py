import os
print os.path.isfile("/")
print os.path.isfile(os.path.expanduser("~/.bashrc"))