from appscript import app

Safari = app('Safari')
if Safari.windows.count():
    print Safari.windows.first.current_tab
    tab=Safari.windows.first.current_tab()
    print Safari.windows.first.current_tab.URL() 
    Safari.windows.first.current_tab.URL.set("http://www.google.com")
    Safari.windows.first.current_tab.set(2)
else:
    print "0 windows"

