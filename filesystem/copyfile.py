from shutil import copy
import sys
m = sys.modules[__name__]
copy(m.__file__,m.__file__+"2")

folder="/Users/nordmenss/git/GISTS/4050474/.git/hooks"
folder2=folder+"2"
copy(folder,folder2)