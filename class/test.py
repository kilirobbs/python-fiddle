class container(object):
	items=[]

	def __init__(self):
		self.items=[]

	def append(self,item):
		self.items.append(item)

class _schema(container):
	def __init__(self):
		super(_schema, self).__init__()
		self.items=[]

	def collect(self):
		self.items.append(schema("name1"))
		self.items.append(schema("name2"))
		self.items.append(schema("name3"))
		self.items.append(schema("name4"))
		#self.append(schema("name1"))
		#self.append(schema("name2"))
		#self.append(schema("name3"))
		#self.append(schema("name4"))

class schema(container):
	name=None
	def __init__(self,name=None):
		self.name=name

schemas=_schema()
schemas.collect()
print container.items