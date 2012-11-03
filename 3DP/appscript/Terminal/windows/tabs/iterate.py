from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

if Terminal.windows.count():
    front_window = Terminal.windows.first
    print "window.name=", front_window.name().encode("utf-8")
    tabs = front_window.tabs()
    for i, tab in enumerate(tabs):
        print "\ntab ", i
        print "custom_title ", tab.custom_title().encode("utf-8")
        print "title_displays_custom_title", tab.title_displays_custom_title()
        #print "contents ", tab.contents()
        #print "history ", tab.history()
else:
    print "0 windows"
