import threading, os

class subclass(threading.Thread):
	value = None
	def __init__(self,value):
		self.value=value
		threading.Thread.__init__(self)

	def run(self):
		print "run"

thread=subclass("test")
thread.start()