#!/usr/bin/env python
from xmlrpclib import ServerProxy
from threading import active_count, Thread


url="http://pypi.python.org/pypi"

pkg="osascript"


class cls(Thread):
    pkg     = None
    session = None

    def __init__(self,pkg):
        self.pkg=pkg
        Thread.__init__(self)

    def run(self):
        pypi=ServerProxy(url)
        response=pypi.package_releases(
            pkg,True
        )
        print response

for i in range(10):
    t=cls(pkg)
    t.start()