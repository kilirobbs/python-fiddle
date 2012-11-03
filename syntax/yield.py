def return_list():
	yield 1 
	yield 2

# yield is iterator 
# http://habrahabr.ru/post/132554/

print return_list()
for value in return_list():
	print value