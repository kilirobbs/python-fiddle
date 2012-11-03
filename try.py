import os
import subprocess


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)     # the exception instance
    # <type 'exceptions.Exception'>
    print inst.args      # arguments stored in .args
    # ('spam', 'eggs')
    print inst
    # ('spam', 'eggs')guard
