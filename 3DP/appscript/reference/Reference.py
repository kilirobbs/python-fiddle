from appscript import app,reference

print app('iCal').__class__
print app('iCal').version.__class__
# <class 'appscript.reference.Reference'>

print reference.Application