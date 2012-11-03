# http://docs.python.org/library/optparse.html
import optparse, os

parser=optparse.OptionParser()

try:
	parser.add_option('-h','--host', type='string')
except:
	pass
parser.add_option('-p','--port', type='string')
import sys
sys.argv.append("192.168.0.38")
sys.argv.append("-p")
sys.argv.append(5433)
options,arguments=parser.parse_args()

for key,value in options.__dict__.items():
    print key,'=',value
for i,item in enumerate(arguments):
    print 'argument #%s = %s'%(i,item)