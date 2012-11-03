import threading

def hello():
    print "hello, world"

# http://docs.python.org/library/threading.html#timer-objects
t = threading.Timer(1.0, hello)
t.start() # after 1 second, "hello, world" will be printed