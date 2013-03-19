from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    for w in Chrome.windows():
        print w().id()
    print "first:",Chrome.windows.first.id()
else:
    print "0 windows"
