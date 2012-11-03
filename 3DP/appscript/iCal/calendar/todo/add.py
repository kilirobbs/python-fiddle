# -*- coding: utf-8 -*-
from appscript import *

def maketodo(title="New ToDo", description="New ToDo", priority=False):
    todo = app('iCal').calendars[u'Напоминания'].todos.end.make(new=k.todo)
    if priority == True:
        todo.priority.set(k.high_priority)
    todo.summary.set(title)
    todo.description.set(description)