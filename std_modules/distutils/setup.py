# http://docs.python.org/distutils/index.html

from distutils.core import setup
setup(name='foo',
      version='1.0',
      py_modules=['foo'], # foo.py
      packages=[ 'foo', ], # /foo
      )