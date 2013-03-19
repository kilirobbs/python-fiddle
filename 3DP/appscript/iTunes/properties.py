from appscript import *

application = app('iTunes')
print application.properties()
print application.frontmost()
print application.version()