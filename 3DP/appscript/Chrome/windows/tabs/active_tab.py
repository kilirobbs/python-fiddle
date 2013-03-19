from appscript import app,k

Chrome = app('Google Chrome')
if Chrome.windows.count():
    tab=Chrome.windows.active_tab
    print tab.URL()
else:
    print "0 windows"