#!/usr/bin/env python
from calendar import timegm
from datetime import datetime, timedelta

def utc_to_local(utc_dt):
    timestamp = timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)


print utc_to_local(datetime.now())