from appscript import app

Chrome = app('Safari')
if Chrome.windows.count():
    print Chrome.windows.first
    Chrome.windows.first().visible.set(False)
    Chrome.windows.first().visible.set(True)
else:
    print "0 windows"
