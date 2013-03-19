#!/usr/bin/env python

from cStringIO import StringIO
from pylint.lint import PyLinter
from pylint.reporters.text import ParseableTextReporter

l = PyLinter()


reporter = ParseableTextReporter()
result = StringIO()
reporter.set_output(result)
l.check(__file__)