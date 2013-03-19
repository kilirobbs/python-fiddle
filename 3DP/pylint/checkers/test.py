#!/usr/bin/env python
from pylint.lint import PyLinter
from pylint import checkers

linter = PyLinter()

checkers.initialize(linter)
linter.quiet = 999
linter.check("errors.py")
s=linter.stats