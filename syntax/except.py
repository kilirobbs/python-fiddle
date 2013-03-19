#!/usr/bin/env python
import sys
from sys import exc_info
import os
try:
    from fixtures import error
    error()
except ImportError:
    print "ImportError"
except Exception, e:
    exc_type, exc_obj, exc_tb = exc_info()
    print "exc_obj",exc_obj
    exc_tb
    print "exc_tb.tb_frame.f_code",exc_tb.tb_frame.f_code
    print "exc_tb.tb_frame.f_code.co_filename",exc_tb.tb_frame.f_code.co_filename
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print exc_type, fname, exc_tb.tb_lineno
    print "Exception=", Exception
    print str(e)
