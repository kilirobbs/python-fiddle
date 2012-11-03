from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')
if Terminal.windows.count():
    window = Terminal.windows.first
    print window.name().encode("utf-8")
else:
    print "0 windows"
