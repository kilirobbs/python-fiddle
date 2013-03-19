# -*- coding: utf-8 -*-
from appscript import app,its,k

#app('iCal').calendars[u'Напоминания'].todos.end.make(new=k.todo)
uid=u"_5ADEBE86-0181-4CFA-A56F-B5A9B39C6D35"
app('iCal').calendars[its.uid==uid].first.todos.end.make(new=k.todo)

