# http://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python

array=[0,10,20,40]
for i in reversed(array):
	print i

print array[::-1]

array.reverse()
print array