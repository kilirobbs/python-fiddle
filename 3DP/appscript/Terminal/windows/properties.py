from appscript import *

Terminal = app(u'/Applications/Utilities/Terminal.app')
Terminal = app('Terminal')
front_window = Terminal.windows.first
print front_window.properties.get()