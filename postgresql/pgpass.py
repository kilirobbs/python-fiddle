import os

# http://www.postgresql.org/docs/current/static/libpq-pgpass.html
# hostname:port:database:username:password

filename=os.getenv("HOME")+"/.pgpass"
exists=os.path.exists(filename)

def lines():
	result=[]
	for l in open(filename,'r').read().splitlines():
		if l.find("#")>0:
			l=l.x[0:l.find("#")-1]
		a=l.split(":")
		if len(a)==5:
			result.append(dict(host=a[0],port=a[1],dbname=a[2],user=a[3],password=a[4]))
	return result

def line(host=None,port=None,dbname=None):
	for l in lines():
		if l["host"] in [host,"*"] \
		and (port is None or int(l["port"]) in [int(port),"*"]) \
		and l["dbname"] in [dbname,"*"]:
			return l

def user(*args,**kwargs):
	try:
		return line(*args,**kwargs)["user"]
	except:
		pass

def password(*args,**kwargs):
	try:
		return line(*args,**kwargs)["password"]
	except:
		pass

print "exists=",exists
print user(host="192.168.0.38",port=5433,dbname="test")
print password(host="192.168.0.38",port=5433,dbname="test")

print user(host="192.168.0.38",port=None,dbname="test")