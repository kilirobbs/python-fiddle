from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')
if Terminal.windows.count():
    windows = Terminal.windows()
    for window in windows:
        print "window.name=", window.name().encode("utf-8")
else:
    print "0 windows"
