from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

if Terminal.windows.count():
    front_window = Terminal.windows.first
    front_window.do_script("clear")
else:
    print "0 windows"
