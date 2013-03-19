#!/usr/bin/env python


d=dict(k="v")
print d["k"] if "k" in d else "default"
print d["k2"] if "k2" in d else None
