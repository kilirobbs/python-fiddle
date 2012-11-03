from threading import Thread

value=0
def count():
	global value
	value+=1

t1 = Thread(target=count)
t1.start()
t2 = Thread(target=count)
t2.start()
t1.join(); t2.join()

print value