from datetime import datetime
from jinja2 import Environment

source="""
{{ datetime.strftime('%Y-%m-%d') }}
"""
tmpl = Environment().from_string(source)
print tmpl.render(
    datetime=datetime.now()
)