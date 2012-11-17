from datetime import datetime
from jinja2 import Environment

class cls:
    id=None
    datetime=None
    def __init__(self,id=None,datetime=None):
        self.id=id
        self.datetime=datetime

source="""
{% for i in items %}
    {% set d = i.datetime %}
    {{ d.year,d.month,d.day }}
    {{ (d.year,d.month,d.day)|join(',') }}
    {{ [d.year,d.month,d.day] }}
{% endfor %}
"""
tmpl = Environment().from_string(source)
now=datetime.now()
items=[cls(id=0,datetime=now),cls(id=1,datetime=now),cls(id=2,datetime=now)]
print tmpl.render(
    items=items
)