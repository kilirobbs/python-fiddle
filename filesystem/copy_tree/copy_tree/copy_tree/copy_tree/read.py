import os

from write import *

f = open('test.txt', 'r')
print f.read()
f.close()

print open('test.txt', 'r').read().splitlines()

print open('test.txt', 'r').read().decode("utf-8")