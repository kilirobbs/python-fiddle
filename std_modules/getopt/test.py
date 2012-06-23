import getopt, sys

# http://www2-pcmdi.llnl.gov/cdat/tips_and_tricks/python_tips/passing_arguments.html

s = '--condition=foo --testing test_value --output-file abc.def -x a1'
args = s.split()
optlist, args = getopt.getopt(args, 'x', ['condition=', 'output-file=', 'testing='])
print optlist, args