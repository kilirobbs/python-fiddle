#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('.')
tmpl = env.get_template('index.html')
print tmpl.render()