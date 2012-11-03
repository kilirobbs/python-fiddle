from appscript import app, its

key="iTunes"
print app('System Events').processes[its.name == key].count()