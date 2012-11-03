from icalendar import Calendar, Event
filename = "/Users/nordmenss/Library/Calendars/FEF22724-F6A1-4EB3-B568-62D339C98CD8.calendar/Events/2AFB30D3-E760-4A91-A323-6E2D50C5489B.ics"
e = Event.from_ical(open(filename, 'rb').read())
for component in e.walk():
    print component.name
    if component.name == "VEVENT":
        print component.get('summary')
        print component.get('dtstart')
        print component.get('dtend')
        print component.get('dtstamp')
