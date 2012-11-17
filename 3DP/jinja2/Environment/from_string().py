from jinja2 import Environment

source="""
{{ var }}
"""
tmpl = Environment().from_string(source)

print tmpl.render(
    var='variable'
)