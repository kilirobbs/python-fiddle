#!/usr/bin/env python
import os

print os.path.exists(__file__)
print os.path.exists([])
# TypeError: coercing to Unicode: need string or buffer, list found

print os.path.exists(1)

from os.path import 