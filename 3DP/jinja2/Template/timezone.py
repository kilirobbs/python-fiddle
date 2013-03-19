from datetime import datetime
from jinja2 import Environment
from pytz import timezone, UTC

source="""
{{ datetime.replace(tzinfo=UTC) }}
"""
tmpl = Environment().from_string(source)
print tmpl.render(UTC=UTC,
    datetime=datetime.now()
)

source="""
{{ datetime.replace(tzinfo=eastern) }}
"""
tmpl = Environment().from_string(source)
print tmpl.render(eastern=timezone('Europe/Moscow'),
    datetime=datetime.now()
)