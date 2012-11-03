def level(path):
	return (path.count("/")+1) / 2

class pg_object():
	oid=None
	path=None
	level=None

	def __init__(self,oid=None,path=None):
		self.oid	= oid
		self.path	= path
		self.level	= level(path)

a=pg_object(1,"SCHEMA/public")
b=pg_object(1,"SCHEMA/public2")
source=dict({a.path:a,b.path:b})
syncing=dict({a.path:a})

diff = list(set(source.keys())-set(syncing.keys()))
print diff
l.sort(key=lambda v:level(v)<0)
#l.sort(key=lambda v: v.find(".sql")<0)