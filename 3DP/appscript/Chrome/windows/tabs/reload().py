from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    Chrome.windows.first.active_tab.reload()
else:
    print "0 windows"