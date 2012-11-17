from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    print Chrome.windows.first.active_tab
    #Chrome.windows.first.active_tab.close()
    print Chrome.windows.first.active_tab.properties()
    print Chrome.windows.first.active_tab.URL
else:
    print "0 windows"
