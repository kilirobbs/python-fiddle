from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    print Chrome.windows.first.active_tab.properties()
    # URL()
    # loading()
    # id()
    # title()
else:
    print "0 windows"