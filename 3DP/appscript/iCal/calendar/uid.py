from time import sleep
from appscript import app,its,k
from envoy import run
app('iCal').quit()
#run("open -a iCal")
try:
    #app('iCal').activate()
    pass
except:
    #app('iCal').activate()
    pass
count=app('System Events').processes[its.name == "iCal"].count()
print "count=",count
while count==0:
    #run("open -a iCal")
    try:
        app('iCal').activate()
    except:
        pass
        #app('iCal').activate()
    sleep(0.001)
    count=app('System Events').processes[its.name == "iCal"].count()
    print "count=",count
print "count=",count