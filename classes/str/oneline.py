class classname():
	value=None
	def __init__(self, value):
		self.value=value

old=classname(value=1)
new=classname(value=-1)

if old.value!=new.value:
	if new.value>0:
		result=">0"
	else:
		result="<0"
else:
	result=""
print result

# is equal to:
test1=False
test2=False
result = "" if old.value==new.value else ">0" if new.value>0 else "<0"
print result


