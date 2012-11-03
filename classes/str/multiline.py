print """1
2
3
"""

name = "extname"
schema = "pg_catalog"

s = (
    "CREATE EXTENSION %(name)s" +
    ("\nWITH SCHEMA " + schema if schema != "public" else "") +
    ("\nWITH SCHEMA " + schema if schema != "public" else "") +
    "\nWITH SCHEMA " + schema if schema != "public" else ""
) % {"name": name}

print s
