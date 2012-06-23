#!/usr/bin/env python
import sys
import os
from optparse import OptionParser

sys.argv.append("-l")

def optional_arg(arg_default):
    def func(option,opt_str,value,parser):
        if parser.rargs and not parser.rargs[0].startswith('-'):
            val=parser.rargs[0]
            parser.rargs.pop(0)
        else:
            val=arg_default
        setattr(parser.values,option.dest,val)
    return func

def main():
        usage = "Usage: test.py"
        parser = OptionParser(usage)
        parser.add_option("-l", "--long",callback=optional_arg('empty'),default=False)

        (options, args) = parser.parse_args()
        if len(args) < 4:
                parser.error("incorrect number of arguments")
        if options.informative:
                print "reading %s..." % options.help

if __name__ == "__main__":
        main()