from appscript import app

Safari = app('Safari')
if Safari.windows.count():
    for i,window in enumerate(Safari.windows()):
        print i,window.properties()
        if i==1:
            window.visible.set(True)
else:
    print "0 windows"
