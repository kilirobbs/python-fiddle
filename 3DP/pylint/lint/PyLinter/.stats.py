#!/usr/bin/env python
from pylint.lint import PyLinter
from pylint import checkers
from pylint.reporters import BaseReporter

linter = PyLinter()

checkers.initialize(linter)
linter.quiet = 999
linter.check("errors.py")
s=linter.stats
print "nb_duplicated_lines",s["nb_duplicated_lines"]
print "undocumented_function",s["undocumented_function"]
print "module",s["module"]
print "warning",s["warning"]
print "badname_const",s["badname_const"]
if "global_note" in s:
    print "global_note",s["global_note"]
print "badname_class",s["badname_class"]
print "undocumented_module",s["undocumented_module"]
print "comment_lines",s["comment_lines"]
print "refactor",s["refactor"]
print "empty_lines",s["empty_lines"]
print "badname_argument",s["badname_argument"]
print "undocumented_class",s["undocumented_class"]
print "docstring_lines",s["docstring_lines"]
print "percent_duplicated_lines",s["percent_duplicated_lines"]
print "fatal",s["fatal"]
print "method",s["method"]
print "function",s["function"]
print "statement",s["statement"]
print "badname_variable",s["badname_variable"]
print "undocumented_method",s["undocumented_method"]
print "by_msg",s["by_msg"]
print "convention",s["convention"]
print "dependencies",s["dependencies"]
#print s["class
print "badname_method",s["badname_method"]
print "by_module",s["by_module"]
print "info",s["info"]
print "badname_module",s["badname_module"]
print "badname_function",s["badname_function"]
print "total_lines",s["total_lines"]
print "error",s["error"]
print "badname_attr",s["badname_attr"]
print "cycles",s["cycles"]