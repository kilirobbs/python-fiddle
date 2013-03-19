print __file__

h=open(__file__)
print h.name

from os import chdir
from os.path import expanduser
chdir(expanduser("~/git"))
print h.name