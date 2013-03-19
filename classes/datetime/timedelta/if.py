#!/usr/bin/env python
from datetime import timedelta

td=timedelta(days=1)
if td:
    print "if"
else:
    print "not if"
    
td=timedelta()
if td:
    print "if"
else:
    print "not if"

