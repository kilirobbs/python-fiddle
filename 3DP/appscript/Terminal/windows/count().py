from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

print "windows count=",Terminal.windows.count()