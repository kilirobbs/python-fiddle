from appscript import *

#app("System Events").application_processes["Terminal.app"].keystroke("w", using=k.command_down)

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')

if Terminal.windows.count() > 0:
    front_window = Terminal.windows.first
    tab = front_window.selected_tab
    tab.custom_title.set("TDD")
    for window in Terminal.windows():
        for tab in window.tabs():
            if tab.custom_title() == "TDD":
                window.close()
else:
    print "0 windows"
