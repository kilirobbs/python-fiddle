from appscript import *

application = app('Terminal')
for window in application.windows():
    print "frontmost", application.frontmost()
    print "name=", application.name()
    print application.version()

#print application.properties()
#print application.startup_settings
