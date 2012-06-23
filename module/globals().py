var=1488

class foo():
	def __init__(self):
		print globals()["var"]

foo()

import sys
from dynamic_import import *
print sys.modules["dynamic_import"].modules