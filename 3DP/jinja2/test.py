#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment

source="""
{{ s.encode("utf-8") }}
"""
tmpl = Environment().from_string(source)
print tmpl.render(s=u"юникод")