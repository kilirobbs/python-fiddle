#!/usr/bin/env python
from appscript import app, its

safari = app('Safari')
print safari.current_tab
safari.current_tab.set(to=1)