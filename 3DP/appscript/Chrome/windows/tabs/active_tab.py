from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    print Chrome.windows.first.active_tab
    Chrome.windows.first.active_tab_index.set(2)
else:
    print "0 windows"