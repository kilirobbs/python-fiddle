from jinja2 import from_string

tmpl = from_string("""
{{ var }}
""")

print tmpl.render(
    var='variable'
)