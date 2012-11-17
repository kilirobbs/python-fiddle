from appscript import app,its,k

Chrome = app('Google Chrome')
if Chrome.windows.count():
    Chrome.windows.first.active_tab.reload()
    id=Chrome.windows.first.active_tab.id()
    print id
    print Chrome.windows.tabs[its.id==id].URL()

else:
    print "0 windows"