# -*- coding: utf-8 -*-
from CalendarStore import CalCalendarStore

store = CalCalendarStore.defaultCalendarStore()
calendars = CalCalendarStore.calendars(store)
predicate = CalCalendarStore.taskPredicateWithCalendars_(calendars)
tasks = store.tasksWithPredicate_(predicate)

for calendar in calendars:
    print ""
    print calendar.uid()
    #print calendar.title()
