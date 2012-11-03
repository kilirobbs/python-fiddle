from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    for window in Chrome.windows():
        print window
        #window.close()
else:
    print "0 windows"
