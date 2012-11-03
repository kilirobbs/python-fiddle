# http://docs.python.org/distutils/index.html


 # http://pypi.python.org/pypi?%3Aaction=list_classifiers
from distutils.core import setup
setup(name='foo',
      version='1.0',
      classifiers=[
      'Environment :: MacOS X',

      'Framework :: Django',

      'License :: OSI Approved :: GNU General Public License (GPL)',

      'Operating System :: MacOS',

      'Natural Language :: English',

      'Topic :: Multimedia :: Sound/Audio',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Software Development :: Version Control'
      'Topic :: Utilities'
      ]
)