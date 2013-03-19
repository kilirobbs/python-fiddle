#!/usr/bin/env python
from os.path import expanduser
from earthtools.sun import load

f=expanduser("~/sun/today.xml")
xml=load(f)
print xml.sunrise
print xml.sunset
print xml.morning.twilight.civil