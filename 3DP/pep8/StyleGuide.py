from os import getcwd
from pep8 import StyleGuide

pep8style = StyleGuide(quiet=True)
r = pep8style.check_files([__file__])
print r.__dict__
print "total_errors",r.total_errors
print "file_errors",r.file_errors
print "line_offset",r.line_offset
print "lines",r.lines
print "filename",r.filename
print "elapsed",r.elapsed
print "_benchmark_keys",r._benchmark_keys
print "expected",r.expected
#print r._ignore_code()
print "counters",r.counters

#pep8style.check_files(paths=[getcwd()]) 
#...path to files/dirs to check...