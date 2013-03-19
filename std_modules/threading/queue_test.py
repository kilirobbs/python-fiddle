#!/usr/bin/env python
from Queue import Queue
from threading import active_count, Thread
from time import sleep
from requests import get

queue = Queue()

THREADS_COUNT = 10

queue.put("http://www.google.ru")

def worker():
    global queue
    while True:
        try:
             url =  queue.get_nowait() 
        except Exception:
            return
        r=get(url)
        print r
        if r:
            pass
        else:
            queue.put(url)

for _ in xrange(THREADS_COUNT):
    thread_ = Thread(target=worker)
    thread_.start()


while active_count() >1:
    print "wait..."
    sleep(1)
print "FINISHED"
