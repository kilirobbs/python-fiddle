from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

if Terminal.windows.count():
    front_window = Terminal.windows.first
    tabs = front_window.tabs()
    for tab in tabs:
        tab.do_script("clear")
else:
    print "0 windows"
