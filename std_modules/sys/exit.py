import sys

# http://stackoverflow.com/questions/285289/exit-codes-in-python
# http://www.wingware.com/psupport/python-manual/2.6/library/sys.html

sys.exit(2)
# Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors.

# In particular, sys.exit("some error message") is a quick way to exit a program when an error occurs.