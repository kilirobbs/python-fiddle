#!/bin/sh

# -a N, -A    depth of research for ancestors
# -s N, -S    depth of research for associated classes
# -A, -S      all ancestors, resp. all associated
# -m[yn]      add or remove the module name
# -f MOD      filter the attributes : PUB_ONLY/SPECIAL/OTHER/ALL
# -k          show only the classes (no attributes and methods)
# -b          show 'builtin' objects


/usr/local/bin/pyreverse -o png -p Pyreverse pgit # package pgit


