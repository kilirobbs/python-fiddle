# http://stackoverflow.com/questions/185936/delete-folder-contents-in-python

import os
import shutil

for root, dirs, files in os.walk('/path/to/folder'):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))

"/Users/nordmenss/git/pg_test"
os.unlink(os.path.join(root, f))