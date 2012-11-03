from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')
if Terminal.windows.count():
    front_window = Terminal.windows.first
    tabs = front_window.tabs()
    for tab in tabs:
        print tab.properties.get()
        print tab.custom_title().encode("utf-8")
else:
    print "0 windows"
