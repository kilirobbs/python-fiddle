from CalendarStore import CalCalendarStore
import CalendarStore
print CalendarStore.__file__
store = CalCalendarStore.defaultCalendarStore()
calendars = CalCalendarStore.calendars(store)
predicate = CalCalendarStore.taskPredicateWithCalendars_(calendars)
tasks = store.tasksWithPredicate_(predicate)
tasks.
for task in tasks:
    completedMark = " "
    completeDate = task.completedDate()
    if completeDate is not None:
        completedMark = "#"
    #print "%s(%s:%s) %s" % (completedMark, task.calendar().title(), task.priority(), task.title())
    print "   uid: %s" % (task.uid())