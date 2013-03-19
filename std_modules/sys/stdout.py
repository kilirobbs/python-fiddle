import sys
from cStringIO import StringIO

def func():
    print "func"

stdout, stderr = sys.stdout, sys.stderr
sys.stdout =c1= StringIO()
sys.stderr =c2= StringIO()
func()
sys.stdout = stdout
sys.stderr = stderr

print "!%s!" % c1.getvalue()
print "!%s!" % c2.getvalue()