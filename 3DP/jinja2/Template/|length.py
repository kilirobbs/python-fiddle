from jinja2 import Environment

source="""
{{ items|length }}
"""
tmpl = Environment().from_string(source)
items=[0,1,2,3]
print tmpl.render(
    items=items
)