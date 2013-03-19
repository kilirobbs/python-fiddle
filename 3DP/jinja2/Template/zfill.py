#!/usr/bin/env python
from jinja2 import Environment

source="""
{{ (0|trim).zfill(2) }}
"""
tmpl = Environment().from_string(source)
print tmpl.render()