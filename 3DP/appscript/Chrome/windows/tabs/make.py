from appscript import app,k

Chrome = app('Google Chrome')
if Chrome.windows.count():
    tab=Chrome.windows.first.tabs.end.make(new=k.tab)
    tab.URL.set("http://www.google.ru/")
else:
    print "0 windows"