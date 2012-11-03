from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')
if Terminal.windows.count():
    windows = Terminal.windows()
    for window in windows:
        window.close()
else:
    print "0 windows"
