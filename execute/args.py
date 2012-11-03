import sys

class args():
	synonims=None
	def __init__(self,synonims=dict()):
		self.synonims = synonims

	@property
	def len(self): return len(sys.argv)

	@property
	def last(self):
		return sys.argv[len(sys.argv)-1] if len(sys.argv)>0 else None

	def value(self,arg):
		return arg.split("=")[1] if len(arg.split("="))>1 else None

	def __getattr__(self,key):
		for i in xrange(0,len(sys.argv)):
			a=sys.argv[i]
			variants=[key]
			if self.synonims.has_key(key):
				variants.append(self.synonims[key])
			for key in variants:
				if a==key or a=="--%s" % key:
					return True
				if a=="-"+key:
					return sys.argv[i+1]

sys.argv=["-h","192.168.0.38","-p","5433","--sql","dbname"]
argv=args(dict(port="p",host="h"))
print "sys.argv=",sys.argv
print ""
print "argv.len=",argv.len
print "argv.host=",argv.host
print "argv.port=",argv.port
print "argv.sql=",argv.sql
print "argv.last=",argv.last
#print ""
#print "argv.dict=",argv.dict