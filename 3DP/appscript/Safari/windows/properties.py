from appscript import app

Safari = app('Safari')
if Safari.windows.count():
    for i,window in enumerate(Safari.windows()):
        print i,window.properties()
        print window.id()
else:
    print "0 windows"
