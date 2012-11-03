import feedparser
import sys
import signal
import time


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException()

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(3)

try:
    time.sleep(0)
    print feedparser.parse("http://github.com/cancerhermit.atom")
except TimeoutException:
    print "timeout"