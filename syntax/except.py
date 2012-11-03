import sys
import os
try:
    some_method()
except ImportError:
    print "ImportError"
except Exception, e:
    print type(e)
    print type(e).__name__
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print "Exception=", Exception
    print str(e)
