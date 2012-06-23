#!/usr/bin/env python
""" Setup file for PyFoo package """

# http://greenmice.info/ru/node/17
 
from distutils.core import setup
setup(name='pyfoo',
      version='1.2.3',
      description='PyFoo package',
      long_description = "PyFoo makes a foo",
      author='Vasya Pupkin',
      author_email='vasya@greenmice.info',
      url='http://greenmice.info/',
      packages=[ 'pyfoo', ],
 
      classifiers=( # http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
        ),
      license="GPL-2"
     )