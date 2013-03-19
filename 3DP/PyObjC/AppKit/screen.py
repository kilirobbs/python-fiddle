from AppKit import NSScreen

frame=NSScreen.mainScreen().frame()
print frame
print frame.origin.x,frame.origin.y
print frame.size.width,frame.size.height