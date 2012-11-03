import threading, time

class MyThread(threading.Thread):
	def run(self):
		time.sleep(5)
		print 'You called my start method, yeah.'
		print 'Were you expecting something amazing?'
		raise BaseException("exception")

thread=MyThread()
print "created"
thread.start()
print "thread.is_alive()=",thread.is_alive()

#thread.join()