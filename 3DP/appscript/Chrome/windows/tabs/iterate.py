from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    for tab in sum(Chrome.windows.tabs(),[]):
        print tab.URL()
else:
    print "0 windows"
