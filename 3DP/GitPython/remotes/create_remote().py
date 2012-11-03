import os
from git import *
dirname = "/Users/nordmenss/git/test"
os.chdir()
repo = Repo.init()
url = 'git://github.com/cancerhermit/Sublime-JS-Beautifier.git'
github = repo.create_remote('github', url)
github.pull(repo.head.reference)