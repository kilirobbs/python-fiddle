#!/usr/bin/env python
from threading import Thread

class subclass(Thread):
	value = None
	def __init__(self,value):
		self.value=value
		Thread.__init__(self)

	def run(self):
		print "run"

thread=subclass("test")
thread.start()