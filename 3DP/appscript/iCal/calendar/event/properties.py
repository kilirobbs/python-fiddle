from appscript import *

for calendar in app('iCal.app').calendars():
    for e in calendar.events():
        d=dict()
        properties=e.properties()
        for key in properties.keys():
            value=getattr(e,str(key).replace("k.",""))()
            if value==k.missing_value:
                value=None
            if type(value)==unicode:
                value=value.encode("utf-8")
            d.update({str(key): value})
        print d