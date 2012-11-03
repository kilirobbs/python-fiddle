from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

if Terminal.windows.count():
    window = Terminal.windows.first
    selected_tab = window.selected_tab
    selected_tab.custom_title.set("mytitle")
    tabs = window.tabs[its.custom_title == 'mytitle']()
    for i, tab in enumerate(tabs):
        print i, tab.custom_title().encode("utf-8")
else:
    print "0 windows"
