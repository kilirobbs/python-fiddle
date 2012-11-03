import os

def hello_world_child():
	print "hello world child"

def hello_world():
	print "hello world"
	hello_world_child()

hello_world()