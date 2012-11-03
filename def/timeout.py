import sys
import signal
import time


class TimeoutException(Exception):
    pass


def get_name():
    def timeout_handler(signum, frame):
        raise TimeoutException()

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(1)  # triger alarm in 3 seconds

    try:
        time.sleep(10)
    except TimeoutException:
        return "default value"
    return name

if __name__ == '__main__':
    name = get_name()
    print "Got: %s" % name,
