from datetime import datetime
import caldav
from caldav.elements import dav, cdav

# http://stackoverflow.com/questions/3758358/how-to-access-apples-ical-server-via-python

# Principal url
url = "https://user:pass@127.0.0.1/user/Calendar"

client = caldav.DAVClient(url)
principal = caldav.Principal(client, url)
calendars = principal.calendars()