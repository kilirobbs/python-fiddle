#!/usr/bin/env python
from os.path import expanduser
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('/'))
env = Environment(loader=FileSystemLoader(["/",expanduser("~"),'.']))

#file="/Users/nordmenss/git/python/tmpl.py/tests/fixtures/template.html"
file="test.html"
template = env.get_template(file)
print template.render(head="head",body="body")
