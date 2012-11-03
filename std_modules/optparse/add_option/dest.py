# http://docs.python.org/library/optparse.html

import optparse, os
parser=optparse.OptionParser()
parser.add_option('-P','--priority', action='count', dest='user_priorety')
parser.add_option('-A','--another', action='count')

import sys
sys.argv.append("-P")
sys.argv.append("-A")
options,arguments=parser.parse_args()

for key,value in options.__dict__.items():
    print key,'=',value