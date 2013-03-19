from appscript import app,its,k

app("Safari").make(new=k.document)
newtab=app("Safari").windows.first.tabs.end.make(new=k.tab)
newtab.URL.set("http://www.google.ru")