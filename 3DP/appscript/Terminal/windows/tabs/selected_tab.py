from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

if Terminal.windows.count():
    front_window = Terminal.windows.first
    tab = front_window.selected_tab
    print "selected_tab custom_title ", tab.custom_title().encode("utf-8")

else:
    print "0 windows"
