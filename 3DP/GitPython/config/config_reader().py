import os
from git import *
repo = Repo("/Users/nordmenss/git/pg_test")
# http://packages.python.org/GitPython/0.3.0/tutorial.html

print repo.config_reader()
# print repo.config_reader(config_level="global").getboolean("user", "name")

print os.getcwd()
os.chdir("/Users/nordmenss/Library/Application Support/Sublime Text 2/Packages/GISTS/3849151")
repo = Repo()  # empty repository, just read config
print repo.config_reader(config_level="global").get("user", "name")

# config_level="repository"
# config_level="global"
# config_level="system"
