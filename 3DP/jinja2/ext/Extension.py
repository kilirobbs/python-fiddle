#!/usr/bin/env python
from jinja2.environment import Environment
from jinja2.ext import Extension

class cls(object):
    name=None
    def __init__(self,value):
        self.name=value

def name(items,value):
    return [v for v in items if v.name==value]

class MyExtension(Extension):
    def __init__(self, environment):
        environment.filters["name"] = name



source="""
{{ items|name("item1") }}
"""
tmpl = Environment(
    extensions=[MyExtension]
).from_string(source)
print tmpl.render(
    items=[cls("item1"),cls("item2"),cls("item3")]
)