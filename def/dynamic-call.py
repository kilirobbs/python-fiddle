import sys
import re
import sys
import os
import re


def function():
    print "function"


class classname():
    def method(self):
        print "method"

instance = classname()
getattr(instance, 'method')()


getattr(sys.modules[__name__], 'function')()
