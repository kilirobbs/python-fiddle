from appscript import app

Chrome = app('Google Chrome')
if Chrome.windows.count():
    print Chrome.windows.first
else:
    print "0 windows"
