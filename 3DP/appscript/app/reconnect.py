from appscript import app
print app('iCal').reconnect()
print app('iCal').AS_appdata.target().reconnect()