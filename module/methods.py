import types
import os, inspect, sys

for a in dir(os):
	if isinstance(os.__dict__.get(a), types.FunctionType):
		f=os.__dict__.get(a)
		print f