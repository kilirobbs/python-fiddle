from appscript import app, its

key="iTunes"
#print app('System Events').processes[its.name == key].count()
#print app('System Events').processes[its.frontmost == True]()[0].name()

print app('System Events').processes[its.name == "VLC"].count()

for p in app('System Events').processes():
    print p.__class__
    print p.properties()